import abc


class BaseGui(abc.ABC):
    """
    Abstract base class for chess GUI implementations.

    Methods
    -------
    start() -> None
        Starts the GUI.
    """

    @abc.abstractmethod
    def start(self) -> None:
        """
        Abstract method that starts the GUI.
        """
