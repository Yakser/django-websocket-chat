from typing import TypedDict


class Message(TypedDict):
    message: str


class WebsocketData(TypedDict):
    username: str
    message: str


class WebsocketEvent(WebsocketData):
    type: str


class ChatMessageEvent(WebsocketEvent):
    type: str
