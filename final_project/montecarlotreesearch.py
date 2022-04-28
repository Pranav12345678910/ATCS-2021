import random


class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("Player 1 is X and Player 2 is O")
        print("The first player to get three in a row of their tile wins")
        return

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        count = 0
        for x in self.board:
            print(str(count), end = '')
            count_2 = 0
            for y in x: 
                if count_2 == 2:
                    print("\t" + y)
                else:
                    print("\t" + y, end = '')
                count_2 += 1
            count += 1
        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        #if it is actually inside the 3x3 grid
        if (row >= 0 and row <= 2) and (col >= 0 and col <= 2):
            #if the tile is not already occupied
            if self.board[row][col] != 'X' and self.board[row][col] != 'O':
                return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given then place the player's icon in the right spot
        user_row = 343434343
        user_col = 343434344
        while self.is_valid_move(user_row, user_col) == False:
            user_row = int(input("Enter a row"))
            user_col = int(input("Enter a col"))
        self.place_player(player, user_row, user_col)
        self.print_board()
        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + " 's Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            self.take_montecarlo_turn(player)
        return

    def take_random_turn(self, player):
        cool_list = [0,1,2]
        row = 23
        col = 23
        while self.is_valid_move(row, col) == False:
            row = random.choice(cool_list)
            col = random.choice(cool_list)
        self.place_player(player, row, col)
        return 

    def take_montecarlo_turn(self, player):
        row = int(self.montecarlo(player)[1])
        col = int(self.monte(player)[2])
        self.place_player(player, row, col)

    def check_col_win(self, player):
        # TODO: Check col win
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[y][x] == player:
                    count += 1
            if y == (len(self.board[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        count = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == player:
                    count += 1
            if y == (len(self.board[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        #if (0,0), (1,1), (2,2) are all equal and all equal to player then return True
        value = 0 
        for x in range(0,len(self.board)): 
            if x == 2:
                break
            for y in range(0,len(self.board[x])):
                if (x + y + 1) == 3:
                    if self.board[x][y] == self.board[x + 1][y - 1] and self.board[x][y] == player:
                        value += 1
        if value == 2:
            return True
        value = 0
        for x in range(0,len(self.board) - 1):
            for y in range(0,len(self.board[x]) - 1):
                if x == y:
                    if self.board[x][y] == self.board[x + 1][y + 1] and self.board[x][y] == player:
                        value += 1
        if value == 2:
            return True

                

    def check_win(self, player):
        # TODO: Check 
        if self.check_col_win(player) == True: 
            return True
        if self.check_diag_win(player) == True:
            return True 
        if self.check_row_win(player) == True:
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        num_occupied = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):  
                if self.board[x][y] != '-':
                    num_occupied += 1
        xwin = self.check_win('X')
        owin = self.check_win('O')
        if num_occupied == 9 and xwin == False and owin == False:
            return True
        return False

    def montecarlo(self, current_state, player):
        #make a new tree
        #make a new root node 
        #set the root node to the current state
        #set the value of the opponent

        #while (program has time):
            #select a node by running selection function

            #if that node does not end game:
                #expand node (find all children)

            #make a new node variable and set it equal to one of the children of the old node randomly, only if it has children
        
            #simulate, store results in a variable, and backpropagate 
        
        #winner = root child with max score
        #return board
        return (opt_row, opt_col)
            

    def play_game(self):
        #TODO: Play game
        player = 'X'
        self.print_instructions()
        while True:
            self.print_board()    
            self.take_turn(player)
            if self.check_win(player) == True:
                print(player + " Wins!")
                break
            if self.check_tie() == True:
                print("Tie!")
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        return