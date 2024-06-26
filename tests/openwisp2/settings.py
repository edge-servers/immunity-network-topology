import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTING = 'test' in sys.argv


DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'immunity_utils.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'immunity_network_topology.db'),
    }
}


SECRET_KEY = '@q4z-^s=mv59#o=uutv4*m=h@)ik4%zp1)-k^_(!_7*x_&+ze$'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'immunity_utils.admin_theme',
    # all-auth
    'django.contrib.sites',
    'immunity_users.accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # controller  (needed to test integration)
    'immunity_controller.pki',
    'immunity_controller.config',
    'immunity_controller.connection',
    'immunity_notifications',
    'immunity_ipam',
    'reversion',
    'sortedm2m',
    'flat_json_widget',
    # network topology
    'immunity_network_topology',
    'immunity_network_topology.integrations.device',
    'immunity_users',
    # admin
    'import_export',
    'admin_auto_filters',
    'django.contrib.admin',
    'django.forms',
    # rest framework
    'rest_framework',
    'drf_yasg',
    'django_filters',
    'rest_framework.authtoken',
    'django_extensions',
    # 'debug_toolbar',
    # channels
    'channels',
]


EXTENDED_APPS = ['django_x509', 'django_loci']

AUTH_USER_MODEL = 'immunity_users.User'
SITE_ID = 1

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'immunity_utils.staticfiles.DependencyFinder',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'immunity2.urls'

ASGI_APPLICATION = 'immunity2.asgi.application'

CHANNEL_LAYERS = {'default': {'BACKEND': 'channels.layers.InMemoryChannelLayer'}}
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'immunity_utils.loaders.DependencyLoader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'immunity_utils.admin_theme.context_processor.menu_groups',
            ],
        },
    }
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'},
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'},
    },
    'formatters': {
        'simple': {'format': '[%(levelname)s] %(message)s'},
        'verbose': {
            'format': '\n\n[%(levelname)s %(asctime)s] module: %(module)s, process: %(process)d, thread: %(thread)d\n%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'main_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR, 'error.log'),
            'maxBytes': 5242880.0,
            'backupCount': 3,
        },
    },
    'root': {'level': 'INFO', 'handlers': ['main_log', 'console', 'mail_admins']},
    'loggers': {'py.warnings': {'handlers': ['console']}},
}

TEST_RUNNER = 'immunity_network_topology.tests.utils.LoggingDisabledTestRunner'

# during development only
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'admin:index'
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

IMMUNITY
_ORGANIZATION_USER_ADMIN = True
IMMUNITY
_ORGANIZATION_OWNER_ADMIN = True
IMMUNITY
_USERS_AUTH_API = True

# Note that the following celery settings
# are intended only for development purposes
# and should not be used in a production environment
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True
CELERY_BROKER_URL = 'memory://'

if not TESTING and any(['shell' in sys.argv, 'shell_plus' in sys.argv]):
    LOGGING.update(
        {
            'loggers': {
                'django.db.backends': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                    'propagate': False,
                }
            }
        }
    )

# Avoid adding unnecessary dependency to speedup tests.
if not TESTING or (TESTING and os.environ.get('WIFI_MESH', False)):
    IMMUNITY
_NETWORK_TOPOLOGY_WIFI_MESH_INTEGRATION = True
    INSTALLED_APPS.insert(
        INSTALLED_APPS.index('immunity_controller.connection'),
        'immunity_controller.geo',
    )
    immunity_ipam_index = INSTALLED_APPS.index('immunity_ipam')
    INSTALLED_APPS.insert(immunity_ipam_index, 'leaflet')
    INSTALLED_APPS.insert(immunity_ipam_index, 'nested_admin')
    INSTALLED_APPS.insert(immunity_ipam_index, 'immunity_monitoring.check')
    INSTALLED_APPS.insert(immunity_ipam_index, 'immunity_monitoring.device')
    INSTALLED_APPS.insert(immunity_ipam_index, 'immunity_monitoring.monitoring')
    TIMESERIES_DATABASE = {
        'BACKEND': 'immunity_monitoring.db.backends.influxdb',
        'USER': 'immunity',
        'PASSWORD': 'immunity',
        'NAME': 'immunity2',
        'HOST': os.getenv('INFLUXDB_HOST', 'localhost'),
        'PORT': '8086',
    }
    IMMUNITY
_MONITORING_MAC_VENDOR_DETECTION = False
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://localhost/9',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            },
        }
    }

if os.environ.get('SAMPLE_APP', False):
    INSTALLED_APPS.remove('immunity_network_topology')
    INSTALLED_APPS.remove('immunity_network_topology.integrations.device')
    EXTENDED_APPS = ['immunity_network_topology']
    INSTALLED_APPS += [
        'immunity2.sample_network_topology',
        'immunity2.sample_integration_device',
    ]
    TOPOLOGY_LINK_MODEL = 'sample_network_topology.Link'
    TOPOLOGY_NODE_MODEL = 'sample_network_topology.Node'
    TOPOLOGY_SNAPSHOT_MODEL = 'sample_network_topology.Snapshot'
    TOPOLOGY_TOPOLOGY_MODEL = 'sample_network_topology.Topology'
    TOPOLOGY_DEVICE_DEVICENODE_MODEL = 'sample_integration_device.DeviceNode'
    TOPOLOGY_DEVICE_WIFIMESH_MODEL = 'sample_integration_device.WifiMesh'

# local settings must be imported before test runner otherwise they'll be ignored
try:
    from .local_settings import *
except ImportError:
    pass
