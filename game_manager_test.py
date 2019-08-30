from tiles import Tiles
from chess_board import ChessBoard
from game_manager import GameManager

WIDTH = 800
HEIGHT = 800
ROW_NUM = 8

def test_constructor():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    assert gm.black_turn == True
    assert gm.WIDTH == 800
    assert gm.HEIGHT == 800

    for y in range(ROW_NUM):
        for x in range(ROW_NUM):
            if y == 3 and x == 3:
                assert gm.tile_list[y][x].color == 'white'
            elif y == 4 and x == 4:
                assert gm.tile_list[y][x].color == 'white'
            elif y == 4 and x == 3:
                assert gm.tile_list[y][x].color == 'black'
            elif y == 3 and x == 4:
                assert gm.tile_list[y][x].color == 'black'
            else:
                assert gm.tile_list[y][x] == None

    assert gm.black_count == 2
    assert gm.white_count == 2
    assert gm.X_ADD == [0, 1, -1, 0, 1, -1, 1, -1]
    assert gm.Y_ADD == [1, 0, 0, -1, 1, -1, -1, 1]
    assert gm.has_input_name == False 
    assert gm.TIME_DURATION == 1500
    assert gm.FILE_NAME == 'scores.txt'


def test_get_legal_move_list():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    white_move_list = gm.get_legal_move_list('black')

    assert white_move_list == {(2, 3): 1,
                               (3, 2): 1,
                               (4, 5): 1,
                               (5, 4): 1}


def test_in_bound():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    assert gm.in_bound(4, 4) == True
    assert gm.in_bound(1, 8) == False
    assert gm.in_bound(2, -1) == False
    assert gm.in_bound(-1, 7) == False
    assert gm.in_bound(9, 3) == False


def test_black_make_move():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    gm.black_make_move(324, 234)
    assert gm.tile_list[2][3].color == 'black'
    assert gm.black_count == 4


def test_decide_next_step():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)
    y, x = gm.decide_next_step()
    
    assert y == 2 and x == 4


def test_white_make_move():
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    gm.white_make_move()

    assert gm.tile_list[2][4].color == 'white'


def test_flip_color():
    # please comment the first line in flip_color
    # function. millis() is not a python statement that can
    # casue error in py test. it is basically a timer recording 
    # time and will not effect the test result.
    cb = ChessBoard(WIDTH, HEIGHT, ROW_NUM)
    tiles = Tiles(cb)
    gm = GameManager(cb, tiles)

    gm.flip_color('white', 3, 2)
    assert gm.tile_list[3][3].color == 'black'



