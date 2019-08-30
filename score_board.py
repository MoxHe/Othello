from tile import Tile
class ScoreBoard:
    def __init__(self, WIDTH, HEIGHT, chess_board, game_manager):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.ORIGIN = chess_board.WIDTH
        self.gm = game_manager
        self.cb = chess_board


    def display(self):
        # draw white score
        fill(1, 1, 1)
        textSize(50) 
        text('Computer', 830, 100)
        textSize(75)
        Tile(self.cb, 'white').display(860, 200)
        text('X ' + str(self.gm.white_count), 920, 225)


        # draw black score
        fill(0, 0, 0)
        textSize(50)         
        text('You', 900, 350)
        textSize(75)
        Tile(self.cb, 'black').display(860, 450)
        text('X ' + str(self.gm.black_count), 920, 475)

        # draw turn
        fill(1)
        if self.gm.black_turn:
            textSize(40)
            string = 'Your turn'
        else:
            textSize(30)
            string = 'Computer\'s turn'

        text(string, self.ORIGIN + self.WIDTH // 2 - textWidth(string) // 2, 700)
