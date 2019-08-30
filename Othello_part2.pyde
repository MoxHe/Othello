from chess_board import ChessBoard
from tile import Tile
from tiles import Tiles
from game_manager import GameManager
from score_board import ScoreBoard


WIDTH = 1100
CB_WIDTH = 800    # chess board width
SB_WIDTH = 300    # score board width 
HEIGHT = 800
ROW_NUM = 8
last_time = millis()
TIME_DURATION = 1500

cb = ChessBoard(CB_WIDTH, HEIGHT, ROW_NUM)
tile = Tile(cb, 'black')
tiles = Tiles(cb)
gm = GameManager(cb, tiles)

sb = ScoreBoard(SB_WIDTH, HEIGHT, cb, gm)

 
def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    global last_time, TIME_DURATION
    background(0, 0.5, 0)
    cb.display()
    sb.display()
    tiles.display()
    if not gm.black_turn:
        if millis() - last_time > TIME_DURATION:
            gm.white_make_move()
    gm.update()
    mouseMoved()
    
    
    
def mousePressed():
    global last_time
    if gm.black_turn:
        last_time = millis()
        
        gm.black_make_move(mouseX, mouseY)   
        global last_time
                 
        
def mouseMoved():
    if gm.black_turn:
        gm.display_potential_tile('black', mouseX, mouseY)
        
