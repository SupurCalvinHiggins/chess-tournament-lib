import chess
import random
from typing import Optional
from .base_engine import BaseEngine
from .engine_result import EngineResult


class RandomEngine(BaseEngine):
    """
    A chess engine that makes random legal moves.
    """

    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        """
        Returns a random legal move for the current chess board state.

        Parameters
        ----------
        board: chess.Board
            The current chess board state.
        time: Optional[float]
            The maximum amount of time to spend searching for a move. Ignored by the RandomEngine.

        Returns
        -------
        result: EngineResult
            The engine result, including a random legal move and no evaluation score.
        """
        move = random.choice(list(board.legal_moves))
        return EngineResult(move=move)
