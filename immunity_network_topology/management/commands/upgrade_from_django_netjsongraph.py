import json
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management import call_command
from django.core.management.base import BaseCommand
from swapper import get_model_name, load_model, split

User = get_user_model()
Topology = load_model('topology', 'Topology')
Organization = load_model('immunity_users', 'Organization')


class BaseUpdateFromDjangoNetjsonGraph(BaseCommand):
    help = 'Upgrade from django-netjsongraph'
    app_label_users = split(get_model_name('immunity_users', 'Organization'))[0]
    app_label = split(get_model_name('topology', 'Topology'))[0]

    def add_arguments(self, parser):
        parser.add_argument(
            '--backup',
            action='store',
            default=settings.BASE_DIR,
            help='(Optional) Path to the backup files',
        )
        parser.add_argument(
            '--organization',
            action='store',
            default=None,
            help=(
                '(Optional) organization UUID of the organization in '
                'which you want to import the data.'
            ),
        )

    def int_to_uuid(self, pk):
        return "00000000-0000-0000-0000-{:012}".format(pk)

    def _get_updated_permission_list(
        self, permission_data, permissions_list, contenttype_data
    ):
        permit_list = []
        for permit_pk in permissions_list:
            for item in permission_data:
                if item['pk'] == permit_pk:
                    for content in contenttype_data:
                        if item['fields']['content_type'] == content['pk']:
                            permit_app_label = content['fields']['app_label']
                            if permit_app_label == 'django_netjsongraph':
                                permit_app_label = self.app_label
                            elif (
                                content['fields']['model'] in ['user', 'group']
                                and permit_app_label == 'auth'
                            ):
                                permit_app_label = self.app_label_users
                    try:
                        permit_list.append(
                            Permission.objects.get(
                                content_type__app_label=permit_app_label,
                                codename=item['fields']['codename'],
                            ).pk
                        )
                    except Permission.DoesNotExist:  # pragma: nocover
                        pass
        return permit_list

    def handle(self, *args, **options):
        if options['organization']:
            org = Organization.objects.get(pk=options['organization'])
        else:
            org = Organization.objects.first()

        # Netjsongraph Models
        with open(f'{options["backup"]}/netjsongraph.json') as netjsongraph:
            netjsongraph_data = json.load(netjsongraph)
        # Make changes
        for data in netjsongraph_data:
            data['fields']['organization'] = str(org.pk)
            data['model'] = f'{self.app_label}.{data["model"].split(".")[1]}'
        # Save in anotherfile
        with open(f'{options["backup"]}/netjsongraph_loaded.json', 'w') as outfile:
            json.dump(netjsongraph_data, outfile)
        # Load to database
        call_command(
            'loaddata', f'{options["backup"]}/netjsongraph_loaded.json', verbosity=0
        )

        # Group Model
        with open(f'{options["backup"]}/contenttype.json') as contenttype:
            contenttype_data = json.load(contenttype)
        with open(f'{options["backup"]}/permission.json') as permission:
            permission_data = json.load(permission)
        with open(f'{options["backup"]}/group.json') as group:
            group_data = json.load(group)
        load_group_data = []
        for data in group_data:
            if not Group.objects.filter(name=data['fields']['name']).exists():
                load_group_data.append(
                    {
                        'model': f'{self.app_label_users}.group',
                        'pk': data['pk'] + Group.objects.count(),
                        'fields': {
                            'name': data['fields']['name'],
                            'permissions': self._get_updated_permission_list(
                                permission_data,
                                data['fields']['permissions'],
                                contenttype_data,
                            ),
                        },
                    }
                )
        if load_group_data:
            # Save in anotherfile
            with open(f'{options["backup"]}/group_loaded.json', 'w') as outfile:
                json.dump(load_group_data, outfile)
            # Load to database
            call_command(
                'loaddata', f'{options["backup"]}/group_loaded.json', verbosity=0
            )

        # User Model
        with open(f'{options["backup"]}/user.json') as users:
            users_data = json.load(users)
        # Make changes
        org_users_data = []
        load_users_data = []
        for data in users_data:
            data['model'] = f'{self.app_label_users}.user'
            data['pk'] = self.int_to_uuid(data['pk'])
            # If the user doesn't have an email, give them a
            # @example.com email but in immunity-network-topology
            # email is UNIQUE.
            if not data['fields']['email']:
                data['fields']['email'] = f'{data["fields"]["username"]}@example.com'
            group_list = []
            for group_pk in data['fields']['groups']:
                for item in group_data:
                    if item['pk'] == group_pk:
                        group_list.append(
                            Group.objects.filter(name=item['fields']['name']).first().pk
                        )
            data['fields']['groups'] = group_list
            data['fields']['user_permissions'] = self._get_updated_permission_list(
                permission_data, data['fields']['user_permissions'], contenttype_data
            )
            if not User.objects.filter(email=data['fields']['email']):
                load_users_data.append(data)
                if not data['fields']['is_superuser']:
                    org_users_data.append(
                        {
                            'model': f'{self.app_label_users}.organizationuser',
                            'pk': str(uuid.uuid4()),
                            'fields': {
                                'created': data['fields']['date_joined'],
                                'modified': data['fields']['date_joined'],
                                'is_admin': False,
                                'user': data['pk'],
                                'organization': str(org.pk),
                            },
                        }
                    )
        load_users_data.extend(org_users_data)
        if load_users_data:
            # Save in anotherfile
            with open(f'{options["backup"]}/user_loaded.json', 'w') as outfile:
                json.dump(load_users_data, outfile)
            # Load to database
            call_command(
                'loaddata', f'{options["backup"]}/user_loaded.json', verbosity=0
            )

        self.stdout.write(self.style.SUCCESS('Migration Process Complete!'))


class Command(BaseUpdateFromDjangoNetjsonGraph):
    pass