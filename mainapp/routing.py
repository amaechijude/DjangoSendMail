from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
        re_path(r'ws/chat/(?P<username>\w+)/$', ChatConsumer.as_asgi()),
    ]


"""from django.urls import re_path

from . import consumers
"""
#websocket_urlpatterns = [
#    re_path(r"ws/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
#]
