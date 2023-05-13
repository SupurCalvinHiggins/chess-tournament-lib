import abc


class BaseGui(abc.ABC):
    @abc.abstractmethod
    def start(self) -> None:
        pass
