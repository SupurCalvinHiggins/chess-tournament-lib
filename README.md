# chess-tournament-lib

Some utilities for a simple custom chess engine tournament with the python-chess package.

## Overview

## Installation

This library requires Python 3.9 or greater. The correct Python version can be downloaded from [here](https://www.python.org/downloads/). Other project dependencies will be installed automatically by **install.bat**.

### Windows

Navigate to the root directory of the repository and execute
```bash
install.bat
```

### Linux

Navigate to the root directory of the repository and execute
```bash
mv install.bat install.sh
chmod +x install.sh
./install.sh
```

## Examples

### FirstMoveEngine

Let's create an engine that makes the first move on the legal move list. We need to create a `FirstMoveEngine` class that inherits from `BaseEngine`.
```python3
import chess
from chess_tournament.engine import BaseEngine

class FirstMoveEngine(BaseEngine):
    pass
```

Now we need to implement the `go` method which takes in a board state and returns the engine's analysis.
```python3
import chess
from chess_tournament.engine import BaseEngine, EngineResult

class FirstMoveEngine(BaseEngine):
    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        move = list(board.legal_moves)[0]
        return EngineResult(move=move)
```

Great! Our engine should be ready analyze games. Let's test it by creating an empty board and asking it to pick a move.
```python3
engine = FirstMoveEngine()
board = chess.Board()
result = engine.go(board, None)
print(result)
```

However, this does not actually make the move on the board. Let's do that now.
```python3
board.push(result.move)
```

But how can we play against another engine? Well `chess_tournament` provides several classes for this purpose. Let's use an `UnlimitedTimeMatch` to play against `RandomEngine` which makes random moves. 
```python3
from chess_tournament.match import UnlimitedTimeMatch
from chess_tournament.engine import RandomEngine

first_move_engine = FirstMoveEngine()
random_engine = RandomEngine()

match = UnlimitedTimeMatch(
    white_engine=first_move_engine, 
    black_engine=random_engine,
)
board = chess.Board()
outcome = match.play(board)
print(outcome)
```

We got the outcome of the game but we couldn't see anything that happened. Let's include a GUI so we can see the match looks like.
```python3
from chess_tournament.gui import TextGui
from chess_tournament.match import UnlimitedTimeMatch
from chess_tournament.engine import RandomEngine

first_move_engine = FirstMoveEngine()
random_engine = RandomEngine()

match = UnlimitedTimeMatch(
    white_engine=first_move_engine, 
    black_engine=random_engine,
)
gui = TextGui(match=match)
gui.start()
```
