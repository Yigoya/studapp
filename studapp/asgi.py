"""
ASGI config for studapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from api.router import websocket_urlspatterns
from api import consumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studapp.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter([
            path('ws/server/<str:rm>',consumer.ChatConsumer.as_asgi()),
            path('ws/server/group/<str:rm>',consumer.GroupConsumer.as_asgi()),
        ])
    )
})
