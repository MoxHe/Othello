class ChessBoard:
    """ Draw and update the chess board"""
    def __init__(self, WIDTH, HEIGHT, ROW_NUM):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.ROW_NUM = ROW_NUM

        self.space = self.WIDTH // self.ROW_NUM 

    def display(self):
        """ Draw the chess board"""
        strokeWeight(3)
        for i in range(self.ROW_NUM + 1):
            # column lines
            line(i * self.space, 0, i * self.space, self.HEIGHT)
            # row lines
            line(0, i * self.space, self.WIDTH, i * self.space)
            
