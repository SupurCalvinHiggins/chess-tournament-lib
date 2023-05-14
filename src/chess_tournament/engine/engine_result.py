import chess
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class EngineResult:
    """
    Immutable data class representing the result of a search performed by a chess engine.

    Attributes
    ---------
    move: chess.Move
        The best move found by the engine.
    score: Optional[float]
        The evaluation of the resulting board position. If None, the engine did not provide an evaluation.
    """

    move: chess.Move
    score: Optional[float] = None
