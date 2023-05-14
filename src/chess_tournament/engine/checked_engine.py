import copy
import chess
from typing import Optional
from .base_engine import BaseEngine
from .engine_result import EngineResult


class CheckedEngine(BaseEngine):
    """
    A CheckedEngine object wraps another engine object and ensures that it only returns legal moves for a given board
    state.
    """

    def __init__(self, engine: BaseEngine) -> None:
        """
        Initializes a CheckedEngine object.

        Parameters
        ----------
        engine: BaseEngine
            The engine object to be checked.

        Returns:
        --------
        None
        """
        self.engine = engine

    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        """
        Returns the best move found by the engine, ensuring it is legal in the current chess board state.

        Parameters
        ----------
        board: chess.Board
            The current chess board state.
        time: Optional[float]
            The maximum amount of time to spend searching for a move. If None, there is no time limit.

        Returns
        -------
        result: EngineResult
            The engine result, including the best move found and the associated evaluation.

        Raises
        ------
        AssertionError:
            If the game is over or if the move found by the engine is illegal in the current board state.
        """
        assert board.outcome() is None
        result = self.engine.go(copy.deepcopy(board), time)
        assert result.move in board.legal_moves
        return result
