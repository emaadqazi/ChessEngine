'''
Handles user input and displaying current GameState object.
'''

import pygame as p
import ChessEngine

p.init() # Initialize pygame up here 

WIDTH = HEIGHT = 1024
DIMENSIONS = 8 # 8x8 dimensions
SQ_SIZE = HEIGHT // DIMENSIONS
MAX_FPS = 15 # For animations later
IMAGES = {}

'''
Initialize global dictionary of images. Will be called once in main.
'''
def loadImages():
    pieces = {'wP', 'wR', 'wN', 'wB', 'wQ', 'wK','bP', 'bR', 'bN', 'bB', 'bQ', 'bK'}
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        # We can acess an image by saying 'IMAGES[piece_name]' as a result of this setup
        
'''
Main driver of the code - handling user input and updating the graphics
'''

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState() # Calling on constructor
    loadImages() # Only do it once before while loop
    running = True 
    sqSelected = () # Initially, no square selected -> keep track of last click of user (tuple: (row, col))
    playerClicks = [] # Keep track of player clicks (two tuples: [(7, 4), (4, 4)]); moving from x,y to x,y
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) location of the mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): # User clicks same square twice
                    sqSelected = () # Deselect
                    playerClicks = [] # Clear the player clicks
                else: # Selecting different square than previously selected
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # Append for both 1st and 2nd clicks
                if len(playerClicks) == 2: # After the 2nd click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected = {} # Reset user clicks so user can make more moves
                    playerClicks = []
                    
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
'''
Responsible for all graphics in current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen) # Draw squares on board
    
    # TODO - add in piece highlighting/move suggestions (future feature)
    
    drawPieces(screen, gs.board) # Draw pieces on top of squares
    
'''
Draw squares on the board. Top left screen is ALWAYS light.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSIONS):
        for c in range (DIMENSIONS):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
'''
Draw pieces on board using current GameState.board variable
'''
def drawPieces(screen, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--": # Piece not empty square
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                

if __name__ == "__main__": # Lets main file work as runnable script and as an importable module
    main()
    
