import chess
from ..gui.gui_callback import GuiCallback
from .base_match import BaseMatch
from ..engine.base_engine import BaseEngine
from ..engine.checked_engine import CheckedEngine


class UnlimitedTimeMatch(BaseMatch):
    """
    A chess match with no time limits.
    """

    def __init__(
        self,
        white_engine: BaseEngine,
        black_engine: BaseEngine,
    ) -> None:
        """
        Initialize the chess match.

        Parameters
        ----------
        white_engine : BaseEngine
            The engine playing as white.
        black_engine : BaseEngine
            The engine playing as black.
        """
        self.white_engine = CheckedEngine(white_engine)
        self.black_engine = CheckedEngine(black_engine)
        self.gui_callbacks = []

    def add_gui_callback(self, gui_callback: GuiCallback) -> None:
        """
        Add a callback to the list of callbacks.

        Parameters
        ----------
        gui_callback : GuiCallback
            The callback function to add to the list of callbacks.
        """
        self.gui_callbacks.append(gui_callback)

    def play(self, board: chess.Board) -> chess.Outcome:
        """
        Play the chess game until a result is reached.

        Parameters
        ----------
        board : chess.Board
            The starting board state for the game.

        Returns
        -------
        chess.Outcome
            The outcome of the game.
        """
        current_engine, next_engine = self.white_engine, self.black_engine
        while board.outcome() is None:
            result = current_engine.go(board, None)
            board.push(result.move)
            current_engine, next_engine = next_engine, current_engine
            for callback in self.gui_callbacks:
                callback(result, board)
        return board.outcome()
