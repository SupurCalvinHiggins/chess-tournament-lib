import chess
from .base_gui import BaseGui
from ..match.base_match import BaseMatch
from ..engine.engine_result import EngineResult


class TextGui(BaseGui):
    def __init__(self, match: BaseMatch) -> None:
        self.match = match
        self.match.add_gui_callback(TextGui.gui_callback)

    @staticmethod
    def gui_callback(result: EngineResult, board: chess.Board) -> None:
        print(f"result = {result}")
        print()
        print(board)

    def start(self) -> None:
        board = chess.Board()
        print(board)
        outcome = self.match.play(board)
        print(f"outcome = {outcome}")
