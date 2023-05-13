import chess
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class EngineResult:
    move: chess.Move
    score: Optional[float] = None
