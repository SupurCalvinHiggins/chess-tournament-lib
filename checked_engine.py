import copy
import chess
from typing import Optional
from base_engine import BaseEngine


class CheckedEngine(BaseEngine):
    def __init__(self, engine: BaseEngine) -> None:
        self.engine = engine

    def go(self, board: chess.Board) -> Optional[chess.Move]:
        assert board.outcome() is None
        move = self.engine.go(copy.deepcopy(board))
        assert move is None or move in board.legal_moves
        return move
