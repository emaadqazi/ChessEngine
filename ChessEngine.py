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
        
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--" # When we move, space we moved from becomes empty
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # Log the move so we can undo it later, or display history
        self.whiteToMove = not self.whiteToMove # Swap players
        
class Move():
    
    # Dictionary, maps keys to values -> key : value 
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} # reverses above ^
    filesToCols =  {"a": 0, "b": 1, "c": 2, "d": 3,
                  "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()} # reverses above
    
    '''
    start: where player was
    endSq: where player ends up
    board: current board state
    '''
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        
    def getChessNotation(self):
        # Real Chess Notation
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
        
    def getRankFile(self, r, c):
        # Rank File Notation
        return self.colsToFiles[c] + self.rowsToRanks[r]