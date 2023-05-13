import chess
from typing import Optional
from gui_callback import GuiCallback
from base_match import BaseMatch
from base_engine import BaseEngine
from checked_engine import CheckedEngine


class UnlimitedTimeMatch(BaseMatch):
    def __init__(
        self,
        white_engine: BaseEngine,
        black_engine: BaseEngine,
    ) -> None:
        self.white_engine = CheckedEngine(white_engine)
        self.black_engine = CheckedEngine(black_engine)
        self.gui_callbacks = []

    def add_gui_callback(self, gui_callback: GuiCallback) -> None:
        self.gui_callbacks.append(gui_callback)

    def play(self, board: chess.Board) -> chess.Outcome:
        current_engine, next_engine = self.white_engine, self.black_engine
        while board.outcome() is None:
            result = current_engine.go(board, None)
            board.push(result.move)
            current_engine, next_engine = next_engine, current_engine
            for callback in self.gui_callbacks:
                callback(result, board)
        return board.outcome()
