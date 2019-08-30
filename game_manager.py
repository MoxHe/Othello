from tile import Tile
from tiles import Tiles

class GameManager:
    """ Control the game, decide winner"""
    def __init__(self, chess_board, tiles):
        self.cb = chess_board
        self.black_turn = True    
        self.WIDTH = self.cb.WIDTH
        self.HEIGHT = self.cb.HEIGHT
        self.tile_list = tiles.tile_list
        # 2 black, 2 white initially
        self.black_count = 2
        self.white_count = 2
        # 8 direction vector
        self.X_ADD = [0, 1, -1, 0, 1, -1, 1, -1]
        self.Y_ADD = [1, 0, 0, -1, 1, -1, -1, 1]
        # flag for inputing name at the end
        self.has_input_name = False 
        # delay time
        self.TIME_DURATION = 1500

        self.FILE_NAME = 'scores.txt'

    def get_legal_move_list(self, color):
        """ Search the entire chess board and get 
        legal move list"""
        # a dict to record legal move and its 
        #corresponding flip counts
        legal_move_list = {}
        # decide which color to flip
        if color == 'black':
            flip_color = 'white'
            terminal_color = 'black'
        else:
            flip_color = 'black'
            terminal_color = 'white'

        # go through every slot
        for y in range(self.cb.ROW_NUM):
            for x in range(self.cb.ROW_NUM):
                # skip empty slot
                if self.tile_list[y][x] is not None:
                    continue
                # search in 8 directions
                for i in range(len(self.X_ADD)):
                    potential_to_flip = []

                    new_y = y + self.Y_ADD[i]
                    new_x = x + self.X_ADD[i]
                    # skip non-flip color situation 
                    if not self.in_bound(new_y, new_x) or \
                       self.tile_list[new_y][new_x] is None or \
                       self.tile_list[new_y][new_x].color == terminal_color:
                        continue
                    # continuously recording in 8 directions until non fip color
                    while self.in_bound(new_y, new_x) and \
                        self.tile_list[new_y][new_x] is not None and \
                        self.tile_list[new_y][new_x].color == flip_color:
                        
                        potential_to_flip.append((new_y, new_x))
                        new_x += self.X_ADD[i]
                        new_y += self.Y_ADD[i]
                    # if it reaches the terminal color at the end, it is valid
                    if self.in_bound(new_y, new_x) and \
                    self.tile_list[new_y][new_x] is not None and \
                    self.tile_list[new_y][new_x].color == terminal_color:

                        # record how many tiles it can fip
                        if (y, x) in legal_move_list:
                            legal_move_list[(y, x)] += len(potential_to_flip)
                        else:
                            legal_move_list[(y, x)] = len(potential_to_flip)

        return legal_move_list


    def in_bound(self, x, y):
        # return true if inside chessboard. 
        return x >= 0 and x < self.cb.ROW_NUM and y >= 0 and y < self.cb.ROW_NUM


    def display_potential_tile(self,color, x, y):
        # display tiles potentially can be placed
        for point in self.get_legal_move_list(color):

            index_x = x // self.cb.space
            index_y = y// self.cb.space

            new_x = index_x * self.cb.space + self.cb.space/2
            new_y = index_y * self.cb.space + self.cb.space/2

            if index_x == point[1] and index_y == point[0]:
                potential = Tile(self.cb, 'grey')
                potential.display(new_x, new_y)
        

    def black_make_move(self, x, y):
        """ Black turn, black make move"""

        # calculate the corresponding index in nested list
        index_x = x // self.cb.space
        index_y = y// self.cb.space

        # if black has legal move
        if (index_y, index_x) in self.get_legal_move_list('black'):
            self.black_count += 1
            
            # change the turn
            self.black_turn = False
            # add next tile to tile list
            next_tile = Tile(self.cb, 'black')
            self.tile_list[index_y][index_x] = next_tile
            self.flip_color('white', index_y, index_x)

            
    def decide_next_step(self):
        # white tile decide next step
        # choose the one that can flip the most black tiles
        legal_move_list = self.get_legal_move_list('white')

        max_flip = 0
        next_step_x = None
        next_step_y = None

        for point in legal_move_list:
            
            current_flip = legal_move_list[point]
            if current_flip > max_flip:
                max_flip = current_flip
                next_step_y = point[0]
                next_step_x = point[1]

        return next_step_y, next_step_x


    def white_make_move(self):
        """ white turn, white make move"""
        index_y, index_x = self.decide_next_step()
        if index_y != None and index_x != None:
            self.black_turn = True
            self.white_count += 1
            # add next tile to tile list
            next_tile = Tile(self.cb, 'white')
            self.tile_list[index_y][index_x] = next_tile

            self.flip_color('black', index_y, index_x)


    def flip_color(self, color, idx_y, idx_x):
        self.start_time = millis()
        if color == 'white':
            flip_color = 'white'
            terminal_color = 'black'
        else:
            flip_color = 'black'
            terminal_color = 'white'
        
        flip_count = 0
        # search in 8 directions
        for i in range(len(self.X_ADD)):

            potential_to_flip = []
            # get adjacent tiles
            new_y = idx_y + self.Y_ADD[i]
            new_x = idx_x + self.X_ADD[i]

            # if not flip color, continue
            if not self.in_bound(new_y, new_x) or \
               self.tile_list[new_y][new_x] is None or \
               self.tile_list[new_y][new_x].color == terminal_color:
                continue

            # continuously recording in 8 directions until non fip color
            while self.in_bound(new_y, new_x) and \
                  self.tile_list[new_y][new_x] is not None and \
                  self.tile_list[new_y][new_x].color == flip_color:

                potential_to_flip.append((new_y, new_x))
                new_x += self.X_ADD[i]
                new_y += self.Y_ADD[i]

            # if reach terminal color
            if self.in_bound(new_y, new_x) and \
               self.tile_list[new_y][new_x] is not None and \
               self.tile_list[new_y][new_x].color == terminal_color:
                
                # flip all tiles in potential_to_flip
                for point in potential_to_flip:
                    self.tile_list[point[0]][point[1]].color = terminal_color

                flip_count += len(potential_to_flip)

        #  update counts
        if terminal_color == 'black':
            self.black_count += flip_count
            self.white_count -= flip_count

        else:
            self.white_count += flip_count
            self.black_count -= flip_count
        
        return flip_count



    def update(self):
        """ Check if the game is over"""
        # If all the tiles have been taken or there are no legal moves
        #  game is finished
        if (self.black_count + self.white_count == self.cb.ROW_NUM ** 2) or \
           (len(self.get_legal_move_list('black')) == 0 and \
           len(self.get_legal_move_list('white')) == 0):

            
            fill(0.8, 0, 0)
            textSize(80)
            # black wins
            res = ""
            if self.black_count > self.white_count:
                res = 'YOU WIN'
            # white wins
            elif self.black_count < self.white_count:
                res = 'COMPUTER WIN'
            # ties
            else:
                res = 'TIE'
            text(res,(self.WIDTH - textWidth(res))// 2, self.HEIGHT/2)

            # if hasn't input name and has delayed for 1.5 second,
            # prompt user input 
            if not self.has_input_name and \
               millis() - self.start_time > self.TIME_DURATION:

                self.has_input_name = True
                name = self.input_name('Enter your name:')
                self.output_score(name, self.black_count)


        # if has black has no legal move, switch turn
        if self.black_turn == True and \
           len(self.get_legal_move_list('black')) == 0 and \
           len(self.get_legal_move_list('white')) != 0:

            self.black_turn = False

        # if white has no legal move
        if self.black_turn == False and \
           len(self.get_legal_move_list('white')) == 0 and \
           len(self.get_legal_move_list('black')) != 0:

            self.black_turn = True


    def input_name(self, message = ''):
        # input name
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)


    def output_score(self, name, score):
        # output name and score, the first line
        # has the highest score
        f = open(self.FILE_NAME, 'r')
        scores = []

        for line in f:
            scores.append(line)
        
        new_score = name + " " + str(score) + '\n'
        if len(scores) == 0:
            scores.append(new_score)
        else:
            if score > int(scores[0].split()[-1]):
                scores.insert(0, new_score)
            else:
                scores.append(new_score)

        f = open(self.FILE_NAME, 'w')
        for line in scores:
            f.write(line)
