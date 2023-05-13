import copy
import chess
from base_engine import BaseEngine


class CheckedEngine(BaseEngine):
    def __init__(self, engine: BaseEngine) -> None:
        self.engine = engine

    def go(self, board: chess.Board) -> chess.Move:
        assert board.outcome() is None
        move = self.engine.go(copy.deepcopy(board))
        assert move in board.legal_moves
        return move
