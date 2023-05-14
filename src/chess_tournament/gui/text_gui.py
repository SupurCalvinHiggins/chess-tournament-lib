import chess
from .base_gui import BaseGui
from ..match.base_match import BaseMatch
from ..engine.engine_result import EngineResult


class TextGui(BaseGui):
    """
    A simple text-based chess GUI that outputs moves and board positions to the console.
    """

    def __init__(self, match: BaseMatch) -> None:
        """
        Initializes the TextGui object with a chess match object.

        Parameters:
        -----------
        match : BaseMatch
            The chess match object to be used for the game. The TextGui object will output the moves and board positions
            from this match object.
        """
        self.match = match
        self.match.add_gui_callback(TextGui.gui_callback)

    @staticmethod
    def gui_callback(result: EngineResult, board: chess.Board) -> None:
        """
        Static method that prints the engine result and the current board position.

        Parameters:
        -----------
        result : EngineResult
            The result of the engine's search, including the best move found and (optionally) an evaluation score.
        board : chess.Board
            The current board position.
        """
        print(f"result = {result}")
        print()
        print(board)

    def start(self) -> None:
        """
        Starts the GUI by initializing the board, playing the match, and printing the final outcome.
        """
        board = chess.Board()
        print(board)
        outcome = self.match.play(board)
        print(f"outcome = {outcome}")
