import chess
import chess.engine
from typing import Optional
from .base_engine import BaseEngine
from .engine_result import EngineResult


class UciEngine(BaseEngine):
    """
    A wrapper for UCI engines like Stockfish.
    """

    def __init__(self, engine_path: str, engine_depth: Optional[int], mate_score: int = 1_000) -> None:
        """
        Construct a new UciEngine. Must be used as a context manager.

        Parameters
        ----------
        engine_path: str
            The path to the UCI engine executable.
        engine_depth: Optional[int]
            The maximum depth the UCI engine is allowed to search. If None, no depth constraints.
        mate_score: int
            Centipawn value to clamp engine scores. Defaults to 1000.
        """
        self.engine: Optional[chess.engine.SimpleEngine] = None
        self.engine_path = engine_path
        self.engine_depth = engine_depth
        self.mate_score = mate_score

    def __enter__(self) -> None:
        """
        Spawns the UCI engine.
        """
        self.engine = chess.engine.SimpleEngine.popen_uci(self.engine_path) # "C:\\stockfish\\stockfish.exe"

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Cleans up the UCI engine.
        """
        self.engine.quit()
        self.engine = None

    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        """
        Returns the UCI engine's evaluation.

        Parameters
        ----------
        board: chess.Board
            The current chess board state.
        time: Optional[float]
            The maximum amount of time to spend searching for a move. If None, then engine_depth must not be None.

        Returns
        -------
        result: EngineResult
            The engine result, including the best move and evaluation.
        """
        assert self.engine is not None
        assert not (time is None and self.engine_depth is None)

        limit = chess.engine.Limit(depth=self.engine_depth, time=time)
        result = self.engine.play(board, limit, info=chess.engine.INFO_SCORE)
        score = result.info["score"].white().score(mate_score=self.mate_score)
        move = result.move
        return EngineResult(move, score=score)
