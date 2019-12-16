from abc import abstractmethod


class Observer:

    @abstractmethod
    def update(self):
        pass


class Observable:

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
