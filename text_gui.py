import chess
from base_gui import BaseGui
from base_match import BaseMatch
from engine_result import EngineResult


class TextGui(BaseGui):
    def __init__(self, match: BaseMatch) -> None:
        self.match = match
        self.match.add_gui_callback(TextGui.gui_callback)

    @staticmethod
    def gui_callback(result: EngineResult, board: chess.Board) -> None:
        print(f"result = {result}")
        print(board)
        print()

    def start(self) -> None:
        self.match.play()
