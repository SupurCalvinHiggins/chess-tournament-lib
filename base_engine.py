import abc
import chess
from typing import Optional


class BaseEngine(abc.ABC):
    @abc.abstractmethod
    def go(self, board: chess.Board) -> Optional[chess.Move]:
        pass
