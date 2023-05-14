import abc
import chess
from .gui_callback import GuiCallback


class BaseMatch(abc.ABC):
    """
    An abstract base class representing a game of chess.
    """

    @abc.abstractmethod
    def add_gui_callback(self, gui_callback: GuiCallback) -> None:
        """
        Abstract method that adds a callback function to be called when a move is made in the game.

        Parameters
        ----------
        gui_callback: GuiCallback
            The callback function to be called when a move is made in the game.
        """

    @abc.abstractmethod
    def play(self, board: chess.Board) -> chess.Outcome:
        """
        Abstract method that plays the game from the given starting position, calls the GUI callbacks when moves are
        made, and returns the outcome of the game.

        Parameters
        ----------
        board: chess.Board
            The starting position of the game.

        Returns
        -------
        chess.Outcome
            The outcome of the game.
        """
