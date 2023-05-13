import chess
import random
from typing import Optional
from base_engine import BaseEngine
from engine_result import EngineResult


class RandomEngine(BaseEngine):
    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        move = random.choice(list(board.legal_moves))
        return EngineResult(move=move)
