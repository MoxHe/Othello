from chess_board import ChessBoard
def test_constructor():
    cb = ChessBoard(800, 800, 8)
    assert cb.WIDTH == 800
    assert cb.HEIGHT == 800
    assert cb.ROW_NUM == 8
    assert cb.space == 100