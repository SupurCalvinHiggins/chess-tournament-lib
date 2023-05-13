import abc
import chess
from gui_callback import GuiCallback


class BaseMatch(abc.ABC):
    @abc.abstractmethod
    def add_gui_callback(self, gui_callback: GuiCallback) -> None:
        pass

    @abc.abstractmethod
    def play(self, board: chess.Board) -> chess.Outcome:
        pass
