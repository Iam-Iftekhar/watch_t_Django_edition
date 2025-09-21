# watch_together/routing.py

from django.urls import re_path

from watch_t.watch_together import consumers

websocket_urlpatterns = [
    # A path to a consumer, for now just a placeholder
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]