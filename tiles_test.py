from chess_board import ChessBoard
from tiles import Tiles

WIDTH = 800
HEIGHT = 800

def test_constructor():
    row_num = 4
    cb = ChessBoard(WIDTH, HEIGHT, row_num)
    tiles = Tiles(cb)
    tile_list = []
    
    for x in range(row_num):
        tile_list.append([])
        for y in range(row_num):
            
            if tiles.tile_list[y][x] == None:
                tile_list[x].append(None)
            else:
                tile_list[x].append(tiles.tile_list[y][x].color)
    
    assert tile_list == [[None, None, None, None],
                         [None, 'white', 'black', None],
                         [None, 'black', 'white', None ],
                         [None, None, None, None]]

