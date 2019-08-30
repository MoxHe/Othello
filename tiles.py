from tile import Tile
class Tiles:
    """ Store and display the all the chess pieces"""
    def __init__(self,chess_board):
        self.cb = chess_board
        # initialise an empty chess list
        self.tile_list = [[None for x in range(self.cb.ROW_NUM)] 
                                for y in range(self.cb.ROW_NUM)]

        # put 4 chess pieces in the middle
        for i in range(self.cb.ROW_NUM//2 - 1, self.cb.ROW_NUM//2 + 1):
            for j in range(self.cb.ROW_NUM//2 - 1, self.cb.ROW_NUM//2 + 1):
                if (i + j) % 2 == 0:
                    self.tile_list[i][j] = Tile(self.cb, 'white')
                else:
                    self.tile_list[i][j] = Tile(self.cb, 'black')

    def display(self):
        """ display all the chesses"""
        for i in range(self.cb.ROW_NUM):
            for j in range(self.cb.ROW_NUM):
                # skip empty slot
                if self.tile_list[i][j] == None:
                    continue
                # calculate corresponding coordinate
                x = j * self.cb.space + self.cb.space/2
                y = i * self.cb.space + self.cb.space/2
                self.tile_list[i][j].display(x,y)