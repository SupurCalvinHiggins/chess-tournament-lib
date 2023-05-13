import chess
import random
from typing import Optional
from base_engine import BaseEngine


class RandomEngine(BaseEngine):
    def go(self, board: chess.Board) -> Optional[chess.Move]:
        return random.choice(list(board.legal_moves))
