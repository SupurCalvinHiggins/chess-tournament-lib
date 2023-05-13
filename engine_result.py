import chess
from typing import Optional


class EngineResult:
    def __init__(self, move: chess.Move, score: Optional[float] = None) -> None:
        self.move = move
        self.score = score
