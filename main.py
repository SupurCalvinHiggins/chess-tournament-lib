from chess_tournament.gui import TextGui
from chess_tournament.match import UnlimitedTimeMatch
from chess_tournament.engine import RandomEngine


if __name__ == "__main__":
    white_engine = RandomEngine()
    black_engine = RandomEngine()
    match = UnlimitedTimeMatch(white_engine, black_engine)
    gui = TextGui(match)
    gui.start()
