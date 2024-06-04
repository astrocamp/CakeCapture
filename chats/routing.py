from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("ws/chatroom/", ChatroomConsumer.as_asgi()),
]
