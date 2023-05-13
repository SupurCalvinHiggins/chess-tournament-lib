import chess
from typing import Callable
from engine_result import EngineResult


GuiCallback = Callable[[EngineResult, chess.Board], None]
