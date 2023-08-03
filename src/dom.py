import rich.repr

from .message_pump import MessagePum

@rich.repr.auto
class DOMNode(MessagePum):
    pass