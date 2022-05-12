import copy 
import time
import random
import math

'''
Article that I adapted pseudocode/general approach from: https://medium.com/swlh/tic-tac-toe-at-the-monte-carlo-a5e0394c7bc2
'''


#keeps track of size of board, what pieces have been played, game status
class board:
    def __init__(self, a_board = None, starting_function = None):       
        '''
        if starting_function == "place":
            print(a_board.board_values)
        '''
        if a_board == None:
            self.board_values = [[0,0,0],[0,0,0],[0,0,0]]
            self.status = 3
        else:
            self.board_values = copy.deepcopy(a_board.board_values)
            '''
            if starting_function == "place":
                print(self.board_values)
            '''
            self.status = copy.deepcopy(a_board.status)
    
    def check_col_win(self, player):
        # TODO: Check col win
        count = 0
        for x in range(len(self.board_values)):
            for y in range(len(self.board_values[x])):
                if self.board_values[y][x] == player:
                    count += 1
            if y == (len(self.board_values[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        count = 0
        for x in range(len(self.board_values)):
            for y in range(len(self.board_values[x])):
                if self.board_values[x][y] == player:
                    count += 1
            if y == (len(self.board_values[x]) - 1):
                if count == 3:
                    return True
            count = 0
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        #if (0,0), (1,1), (2,2) are all equal and all equal to player then return True
        value = 0 
        for x in range(0,len(self.board_values)): 
            if x == 2:
                break
            for y in range(0,len(self.board_values[x])):
                if (x + y + 1) == 3:
                    if self.board_values[x][y] == self.board_values[x + 1][y - 1] and self.board_values[x][y] == player:
                        value += 1
        if value == 2:
            return True
        value = 0
        for x in range(0,len(self.board_values) - 1):
            for y in range(0,len(self.board_values[x]) - 1):
                if x == y:
                    if self.board_values[x][y] == self.board_values[x + 1][y + 1] and self.board_values[x][y] == player:
                        value += 1
        if value == 2:
            return True
        return False

    def find_empty_spaces(self):
        #2d List that will contain coordinates of empty spaces
        empty_spaces = []
        for x in range(0,len(self.board_values)): 
            for y in range(0,len(self.board_values[x])):
                #each spot starts out as 0 so if its 0 that means its empty
                if self.board_values[x][y] == 0:
                    empty_spaces.append([x,y])
        return empty_spaces

    def check_win(self, player):
        # TODO: Check 
        if self.check_col_win(player) == True: 
            return (True, player)
        if self.check_diag_win(player) == True:
            return (True, player)
        if self.check_row_win(player) == True:
            return (True, player)
        return (False, player)
    
    def check_tie(self):
        for x in self.board_values:
            for y in x:
                if y == 0:
                    return False
        return True

    def find_opposite_player_again(self, player_input):
        if player_input == 'X':
            return 'Y'
        return 'X'
        
    def check_status(self, player):
        #needs to return-1/0/1/3 W for other player/Tie/Win for player/In progress
        if self.check_win(player)[0] == True:
            return 1
        elif self.check_win(self.find_opposite_player_again(player))[0] == True:
            return -1
        elif self.check_tie() == True:
            return 0
        else:
            return 3

    def take_manual_turn(player):
        row = -1
        col = -1
        while (row < 1 or row > 2) and (col < 1 or col > 2):
            row = int(input("What row do you want to insert your player in? Input an integer from 0 - 2: "))
            col = int(input("What col do you want to insert your player in? Input an integer from 0 - 2: "))
        return (row, col)

#keeps track of current player, board, score of the node, win score of node 
class state:
    def __init__(self, a_board = None, state = None):
        if a_board != None and state == None: #if they have only have a board for the node
            self.player_number = None
            self.a_board = board(a_board)
            self.num_wins = 10
            self.visit_count = 0    
        elif a_board != None and state != None: #if they want to clone a state
            self.player_number = state.player_number
            self.a_board = board(a_board)
            self.num_wins = state.num_wins
            self.visit_count = state.visit_count
        else: #if I have no info and just want to make a new state
            self.a_board = board()
            self.player_number = None
            self.num_wins = 10
            self.visit_count = 0

    def find_opposite_player(self):
        if self.player_number == 'X':
            return 'Y'
        return 'X'

    def random_playout(self):
        #random play: 1. get available positions 2. Find random index in available positions array 3. perform move on that randomly selected position
        available_spots = self.a_board.find_empty_spaces()
        index = random.randint(0, len(available_spots) - 1)
        #2 element long array, where 1st index is row and 2nd index is column
        coords = available_spots[index]
        self.a_board.board_values[coords[0]][coords[1]] = self.player_number

    def switch_player(self):
        if self.player_number == 'X':
            self.player_number = 'Y'
            return
        self.player_number = 'X'
    
    def switch_player_return(self):
        if self.player_number == 'X':
            return 'Y'
        return 'X'

    #returns new board with symbol at coords
    def do_move(self, coords, symbol):
        new = board(self.a_board)
        new.board_values[coords[0]][coords[1]] = symbol 
        return new

    def compute_neighbors(self):
        available_spots = self.a_board.find_empty_spaces()
        neighboring_states = []
        for x in available_spots:
            neighboring_states.append(state(self.do_move(x, self.switch_player_return())))
        return neighboring_states


#keeps track of the state
class node:
    def __init__(self, a_state = None, a_node = None):
        if a_node == None and a_state != None: #
            self.a_state = a_state
            self.child_array = []
            self.parent_node = None
        elif a_node != None and a_state != None: 
            self.a_state = a_state(None, a_node.a_state) 
            if a_node.parent_node != None:
                self.parent_node = a_node.parent_node
            self.child_array = [] 
            for x in a_node.child_array:
                self.child_array.append(a_node(None, x))
        else:
            self.a_state = state()
            self.parent_node = None
            self.child_array = []
    
    def pick_random_child(self):
        index = random.randint(0, len(self.child_array) - 1)
        return self.child_array[index]

    def find_highest_visit_count(self):
        visit_counts = []
        for x in self.child_array:
            visit_counts.append(x.a_state.visit_count)
        max_value = max(visit_counts)
        return self.child_array[visit_counts.index(max_value)]


#used to create nodes
class Tree:
    def __init__(self, new_node = None):
        if new_node != None:
            self.root = new_node
        else:
            self.root = node()

def calc_ucb(total_sims, num_wins, num_node_sims):
    if num_node_sims == 0:
        #have to return a huge number so that this unvisited node gets visited at least a little bit 
        return 2000000000000000000000
    return (num_wins/num_node_sims) + 1.41 * math.sqrt(math.log(total_sims) / num_node_sims)

def find_best_ucb(input_node):
    parent_visit_count = input_node.a_state.visit_count
    #the 1st index will be the UCB value of the 1st child node, 2nd index will be the UCB value of the 2nd child node, etc  
    child_ucb = [] 
    for x in input_node.child_array:
        child_ucb.append(calc_ucb(parent_visit_count, x.a_state.num_wins, x.a_state.visit_count))
    #the indices of child_ucb and child_array match which is why returning the index is important
    return input_node.child_array[child_ucb.index(max(child_ucb))]

def selection(root_node):
    #starts as root node
    child_node = root_node
    while len(child_node.child_array) > 0:
        #takes on value of best child node of node that was passed into function
        child_node = find_best_ucb(child_node)
    return child_node

#all this function does is fill up the child_array function in the node class, unless 
#the node represents a win, loss, or tie 
def expand_node(node_to_expand):
    #this function gets all the possible outcomes from node 
    neighboring_nodes = node_to_expand.a_state.compute_neighbors()

    #x represents one of the potential states we can get from the node that was passed in
    #already have neighboring states, only need to convert them into nodes and add them to node_to_expand's child array
    for x in neighboring_nodes:
        temp_node = node(x)
        temp_node.parent_node = node_to_expand
        temp_node.a_state.player_number = temp_node.a_state.find_opposite_player()
        node_to_expand.child_array.append(temp_node)
    return node_to_expand.child_array
    
#same function as before but need it to be outside of state class as well
def find_opposite_player_2(player):
    if player == 'X':
        return 'Y'
    return 'X'

#returns a tuple of (result, player)
def random_simulation(start_node, opposing_player):
    temp_node = node(None, start_node)
    temp_state = temp_node.a_state
    #board_status possible values:1 if opposing player won, 0 if tie, -1 if player opposite to opposing_player won (player) and 3 if in progress
    board_status = temp_state.a_board.check_status(opposing_player)
    
    #if this node results in a victory for the opponent, it will avoid that move 
    if board_status == 1:
        temp_node.parent_node.state.num_wins = -200000000000
        return (board_status, opposing_player)

    current_player = opposing_player
    while board_status == 3:
        temp_state.switch_player()
        current_player = find_opposite_player_2(current_player)
        temp_state.random_playout()
        board_status = temp_state.a_board.check_status(current_player)
    return (board_status, current_player)

def backpropagate(node_to_explore, winning_player):
    temp_node = node_to_explore
    while temp_node != None:
        temp_node.a_state.visit_count += 1
        if temp_node.a_state.player_number == winning_player:
            temp_node.a_state.num_wins += 10
        temp_node = temp_node.parent_node

#returns a new game board
def montecarlo(game_board, player):
    opponent = find_opposite_player_2(player)
    tree = Tree()
    root_node = tree.root
    temporary_board = copy.deepcopy(game_board)
    temporary_state = state(temporary_board)
    root_node = node(temporary_state)
    root_node.a_state.player = player #'X' for the first time

    now = time.time()
    #I decided to give the while loop 1.5 seconds of allotted time. Once the 1.5 seconds are up the while loop ends
    while ((time.time() - now) < 1.5):
        new_node = selection(root_node)
        
        if new_node.a_state.a_board.check_win(player)[0] == False:
            new_node.child_array = expand_node(new_node) 

        node_to_explore = new_node
        if len(node_to_explore.child_array) > 0:
            node_to_explore = new_node.pick_random_child()
    
        result = random_simulation(node_to_explore, opponent)
        #print(result)
        backpropagate(node_to_explore, result) 
        print(node_to_explore.a_state.num_wins)
        print(node_to_explore.a_state.visit_count)
    
    #find child of root node that has the highest visit count, because that has the highest chance of being a good move
    chosen_node = root_node.find_highest_visit_count()
    #return the board of the chosen node so that it can be used as the game board
    return chosen_node.a_state.a_board

def print_instructions():
        # TODO: Print the instructions to the game
        print("Player 1 is X and Player 2 is O")
        print("The first player to get three in a row of their tile wins. The number 0 signifies a blank tile")
        return

def print_board(bored):
    # TODO: Print the board
    print("\t0\t1\t2")
    count = 0
    for x in bored.board_values:
        print(str(count), end = '')
        count_2 = 0
        for y in x: 
            if count_2 == 2:
                print("\t" + str(y))
            else:
                print("\t" + str(y), end = '')
            count_2 += 1
        count += 1
    return

#finds differences 
def find_montecarlo_turn(old_board, player):
    new_board = montecarlo(old_board, player)
    coords_and_player = []
    for x in range(len(old_board.board_values)):
        for y in range(len(old_board.board_values)):
            if old_board.board_values[x][y] != new_board.board_values[x][y]:
                coords_and_player.append((x,y))
                coords_and_player.append(player)
    return tuple(coords_and_player)
    
def play_game():
    #TODO: Play game
    current_player = 'X'
    game_board = board()
    print_instructions()
    while True:
        print_board(game_board)
        if current_player == 'X':
            #the move is a tuple that contains two elements: a 2 element long tuple of coordinates, and the player
            move = find_montecarlo_turn(game_board, 'X')
            row = move[0][0]
            col = move[0][1]
            game_board.board_values[row][col] = move[1]
            #print(str(game_board.board_values) + '2')
            #take random turn gets input fromn the user of an unoccupied row and col and puts the player there
            #game_board.take_manual_turn()
        else:
            user_coords = game_board.take_manual_turn()
            row_2 = user_coords[0]
            col_2 = user_coords[1]
            
            game_board.board_values[row_2][col_2] = 'Y'
        if game_board.check_win(current_player)[0] == True:
            print(game_board.board_values)
            print(current_player + " Wins!")
            break
        if game_board.check_win(find_opposite_player_2(current_player))[0] == True:
            print(game_board.board_values)
            print(find_opposite_player_2(current_player) + "Wins!")
        #check tie simply checks if every tile is occupied, so checking win first is necessary
        if game_board.check_tie() == True:
            print("Tie!")
            break
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    return

play_game()


'''
test_board = board()
test_board.board_values = [['X', 'X', 'X'],['Y', 0, 'Y'],[0, 'Y', 0]]
print(test_board.check_win('X'), test_board.check_diag_win('X'), test_board.check_col_win('X'), test_board.check_row_win('X'))
'''

#To - Do: Fix check_win

#Problem: The algorithm is just picking the same spots over and over again, going in row major order down the board values list


#I initially thought the above Problem (it picking the same spots always) was in the simulation phase of the algorithm, because
#Board status is always 0 every single time meaning it is always simulating until a tie
#Which must mean check_win is not working
#This also makes sense because num_wins never changes
#Other reason why check_win seems to not work is because the game never ends

#I fixed the check_status function (but not check_win, even though check_win seems to work in every scenario except play_game())
#However game is still never ending

#The problem is probably in backpropagation


#When I print out num_wins and visit_count, visit_count increases but num_wins doesn't further suggesting that num_wins isn't increasing

#Latest update: check_win is now working. It was always working, but I forgot it returned a tuple and was checking the value of the entire thing instead of just the first index.
#The program still picks coordinates in row - major order. It still runs and works fine from the outside. But the inner logic is dysfunctional. The num_wins variable is still not changing