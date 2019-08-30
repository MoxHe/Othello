from chess_board import ChessBoard
from game_manager import GameManager
from tiles import Tiles
from score_board import ScoreBoard

WIDTH = 800
HEIGHT = 800
ROW_NUM = 8

def test_constructor():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    gm = GameManager(cb, Tiles(cb))
    sb = ScoreBoard(200, 800, cb, gm)

    assert sb.WIDTH == 200
    assert sb.HEIGHT == 800