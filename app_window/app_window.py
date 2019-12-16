from abc import abstractmethod


class AbsAppWindow:

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def start_timer(self):
        pass
