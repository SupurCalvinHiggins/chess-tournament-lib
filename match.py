import chess
from base_engine import BaseEngine
from checked_engine import CheckedEngine


class Match:
    def __init__(self, white_engine: BaseEngine, black_engine: BaseEngine) -> None:
        self.white_engine = CheckedEngine(white_engine)
        self.black_engine = CheckedEngine(black_engine)

    def play(self) -> chess.Outcome:
        board = chess.Board()
        current_engine, next_engine = self.white_engine, self.black_engine
        while board.outcome() is None:
            result = current_engine.go(board, None)
            board.push(result.move)
            current_engine, next_engine = next_engine, current_engine
        return board.outcome()
