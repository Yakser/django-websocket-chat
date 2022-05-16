class WebsocketEventType:
    type: str = 'base-websocket-event'

    def __str__(self):
        return self.type

    def __repr__(self):
        return f"WebsocketEvent<{self.type}>"


class ChatMessageEventType(WebsocketEventType):
    type: str = 'chat-message'
