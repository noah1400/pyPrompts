
class EventsMixin:

    listeners: dict = {}

    def on(self, event: str, callback: callable) -> None:
        if event not in self.listeners:
            EventsMixin.listeners[event] = []

        EventsMixin.listeners[event].append(callback)

    def emit(self, event: str, *args) -> None:
        if event in EventsMixin.listeners:
            for listener in EventsMixin.listeners[event]:
                listener(*args)

    def clearListeners(self) -> None:
        self.listeners = {}