import abc
import chess


class BaseEngine(abc.ABC):
    @abc.abstractmethod
    def go(self, board: chess.Board) -> chess.Move:
        pass
