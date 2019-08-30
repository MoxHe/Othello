from chess_board import ChessBoard
from tile import Tile

WIDTH = 800
HEIGHT = 800
ROW_NUM = 8

def test_constructor():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tile = Tile(cb, 'black')
    assert tile.color == 'black'
    assert tile.CLEARANCE == 10
    assert tile.width == 90
    assert tile.height == 90
