import copy
import chess
from typing import Optional
from base_engine import BaseEngine
from engine_result import EngineResult


class CheckedEngine(BaseEngine):
    def __init__(self, engine: BaseEngine) -> None:
        self.engine = engine

    def go(self, board: chess.Board, time: Optional[float] = None) -> EngineResult:
        assert board.outcome() is None
        result = self.engine.go(copy.deepcopy(board))
        assert result.move in board.legal_moves
        return result
