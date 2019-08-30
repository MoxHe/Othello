class Tile:
    """ Define a single chess piece"""
    def __init__(self, chess_board, color):
        self.cb = chess_board
        self.color = color
        self.CLEARANCE = 10
        self.width = self.cb.space - self.CLEARANCE
        self.height = self.cb.space - self.CLEARANCE

    def display(self, x, y):
        """ Display the chess piece"""
        strokeWeight(3)
        if self.color == 'black':
            fill(0)
        if self.color == 'white':
            fill(1)
        if self.color == 'grey':
            fill(0.5, 0.5, 0.5)
        ellipse(x, y, self.width, self.height)


    def __repr__(self):
        """ print the chess"""
        return self.color
