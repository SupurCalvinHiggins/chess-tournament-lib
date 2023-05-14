import abc
import chess
from typing import Optional
from .engine_result import EngineResult


class BaseEngine(abc.ABC):
    @abc.abstractmethod
    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        """
        Given a board state and remaining clock time, return the next best move.

        Parameters
        ----------
        board: chess.Board
            The board state to analyze.
        time: Optional[float]
            The remaining clock time. If None, there are no time constraints.

        Returns
        -------
        EngineResult
            The result of the engine's analysis.
        """
