import abc
import chess
from typing import Optional
from engine_result import EngineResult


class BaseEngine(abc.ABC):
    @abc.abstractmethod
    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        pass
