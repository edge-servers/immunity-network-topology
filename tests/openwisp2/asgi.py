from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf import settings

if 'immunity_controller.geo' in settings.INSTALLED_APPS:
    from immunity_controller.routing import get_routes as get_controller_routes
else:
    from immunity_controller.connection.channels.routing import (
        get_routes as get_connection_routes,
    )
    from immunity_notifications.websockets.routing import (
        get_routes as get_notification_routes,
    )

    def get_controller_routes():
        return get_connection_routes() + get_notification_routes()


import immunity_network_topology.routing

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                immunity_network_topology.routing.websocket_urlpatterns
                + get_controller_routes()
            )
        ),
    }
)
