import abc
import chess


class BaseMatch(abc.ABC):
    @abc.abstractmethod
    def play(self) -> chess.Outcome:
        pass
