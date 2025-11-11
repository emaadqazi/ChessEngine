'''
Responsible for storing information about current state of chess game.
Also responsible for determining the valid moves at the current state.
Will also keep a move log (allow us to undo move, go forward, etc).
'''

class GameState():
    def __init__(self):
        # Board is 8x8, 2D list
        # Each element in list has 2 characters: (1) color of piece (2) type of piece:
        # R = Rook, N = Knight, B = Bishop, Q = Queen, K = King, P = Pawn
        # "--" represents empty space
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.whiteToMove = True
        self.moveLog = []