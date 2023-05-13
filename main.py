from text_gui import TextGui
from unlimited_time_match import UnlimitedTimeMatch
from random_engine import RandomEngine


if __name__ == "__main__":
    white_engine = RandomEngine()
    black_engine = RandomEngine()
    match = UnlimitedTimeMatch(white_engine=white_engine, black_engine=black_engine)
    gui = TextGui(match)
    gui.start()