from channels.routing import route

channel_routing = [
    # Customize routes used for sockets
    route("test", "app.consumers.http_consumer"),
]
