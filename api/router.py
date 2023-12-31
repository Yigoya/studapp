from django.urls import path
from . import consumer

websocket_urlspatterns = [
    path('ws/server/<int:rm>',consumer.ChatConsumer.as_asgi())
]