from typing import TypedDict

from websockets.events import ChatMessageEventType, WebsocketEventType


class Message(TypedDict):
    message: str


class WebsocketData(TypedDict):
    username: str
    message: str


class WebsocketEvent(WebsocketData):
    type: WebsocketEventType


class ChatMessageEvent(WebsocketEvent):
    type: ChatMessageEventType
