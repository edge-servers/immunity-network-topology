import os

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from immunity_users.api.urls import get_api_urls

urlpatterns = []

if os.environ.get('SAMPLE_APP', False):
    from immunity_network_topology.utils import get_visualizer_urls

    from .sample_network_topology.visualizer import views

    urlpatterns += [path('topology/', include(get_visualizer_urls(views)))]

urlpatterns += [
    path('', include('immunity_network_topology.urls')),
    # needed to test integrations
    path('', include('immunity_controller.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('immunity_utils.api.urls')),
    path('api/v1/', include(get_api_urls())),
]

urlpatterns += staticfiles_urlpatterns()
if 'immunity_monitoring.monitoring' in settings.INSTALLED_APPS:
    urlpatterns.append(path('', include('immunity_monitoring.urls')))

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
