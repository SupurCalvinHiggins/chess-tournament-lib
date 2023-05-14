import chess
import chess.pgn
from typing import Optional
from chess_tournament.engine import RandomEngine
from chess_tournament.engine import BaseEngine, EngineResult


class InputEngine(BaseEngine):
    """
    A chess engine that allows the user to input moves.
    It will display the board, and an enumerated list of legal moves for the user to choose from
    The user choses a number to make a move, which is then returned if the input is valid
    If not, it repeats getting user input until it is.
    """
    def go(self, board: chess.Board, time: Optional[float]) -> EngineResult:
        print("The board is:")
        print(board.unicode())
        moves = list(board.legal_moves)
        print("The legal moves are")
        for i,m in enumerate(moves):
            print(str(i) + ": " + self.move_to_readable_move(board, m))
        
        while True:
            choice = input("Select one of the moves using their number:\n")
            try:
                move = moves[int(choice)]
                return EngineResult(move=move)
            except Exception as e:
                print("Your input was invalid, try again")
    
    
    def move_to_readable_move(self, board: chess.Board, move: chess.Move):
        """
        Given a board state and a move, return a string representing the move
        using language better readable by chess players
        
        Parameters
        ----------
        board: chess.Board
            The board state to analyze.
        move: chess.Move
            The move to make a string for
        
        Returns
        -------
        str
            The string representation of the input move
        """
        uci = move.uci()
        files = ['a','b','c','d','e','f','g','h']
        origin_file = ord(uci[0]) - 97
        origin_rank = int(uci[1]) - 1
        dest_file = ord(uci[2]) - 97
        dest_rank = int(uci[3]) - 1
        
        origin_sqaure = chess.square(origin_file, origin_rank)
        piece = board.piece_at(origin_sqaure)
        
        attacked_square = chess.square(dest_file, dest_rank)
        attacked_piece = board.piece_at(attacked_square)
        
        ascii_piece = ""
        unicode_piece = ""
        output = ""
        
        if piece.piece_type != chess.PAWN:
            unicode_piece = piece.unicode_symbol()
            ascii_piece = piece.symbol().upper()
            
            attacking_sqaures = board.attackers(board.turn,attacked_square)
            same_piece_sqaures = []
            specify_position = False
            for a_sqaure in attacking_sqaures:
                if a_sqaure != origin_sqaure and board.piece_type_at(a_sqaure) == piece.piece_type:
                    same_piece_sqaures.append(a_sqaure)
                    specify_position = True
            
            specify_rank = False
            for s in same_piece_sqaures:
                are_same_type = board.piece_type_at(a_sqaure) == piece.piece_type
                if chess.square_file(s) == chess.square_file(origin_sqaure) and are_same_type:
                    specify_rank = True
                    
            if specify_position:
                if specify_rank:
                    output += str(origin_rank + 1)
                else:
                    output += files[origin_file]
                    
        else:
            if board.piece_at(attacked_square) != None:
                ascii_piece += files[origin_file]
                unicode_piece = ascii_piece
        
        
        if attacked_piece != None:
            output += "x"
            
        output += files[dest_file] + str(dest_rank + 1)
        
        if board.gives_check(move):
            turn = board.turn
            test_board = board.copy()
            test_board.turn = turn
            test_board.push(move)
            outcome = test_board.outcome()
            if outcome != None and outcome.winner == turn:
                output += "#"
            else:
                output += "+"
            
        return ascii_piece + output + " (" + unicode_piece + output + ")"