import copy 
import time

#keeps track of size of board, what pieces have been played, game status
class board:
    def __init__(self, board): 
        if board == None:
            self.board_values = [[0,0,0],[0,0,0],[0,0,0]]
            self.IN_PROGRESS == -1
        else:
            self.board_values = copy.copy(board.board_values)
            self.IN_PROGRESS = -1
            self.DRAW = 0
            self.total_moves = 0
            self.P1 = 0
            self.P2 = 0
    
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
            return 

    def find_empty_spaces():
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
            return True
        if self.check_diag_win(player) == True:
            return True 
        if self.check_row_win(player) == True:
            return True
        return False

#keeps track of current player, board, score of the node, win score of node 
class state:
    def __init__(self, board, state):
        if board != None and state == None: #if they have only have a board for the node
            self.player_number = None
            self.board = Board(board)
            self.num_wins = 10
            self.visit_count = 0    
        elif board != None and state != None: #if they want to clone a state
            self.player_number = state.player_number
            self.board = Board(board)
            self.num_wins = state.num_wins
            self.visit_count = state.visit_count
        else: #if I have no info and just want to make a new state
            self.board = Board()
            self.player_number = None
            self.num_wins = 10
            self.visit_count = 0

        def find_opposite_player():
            if self.player_number == 'X':
                return 'Y'
            return 'X'

        def compute_neighbors():
            available_spots = self.board.find_empty_spaces()
            neighboring_states = []
            for x in available_spots:
                temp_board = board()
                temp_board.board_values[x[0],x[1]] = self.find_opposite_player()
                temp_state = state(temp_board)
                neighboring_states.append(temp_state)
            return neighboring_states

            
#keeps track of the state
class node:
    def __init__(self, state, node):
        if node == None and state != None: #
            self.state = state
            self.child_array = []
            self.parent_node = None
        elif node != None and state != None: 
            self.state = new state(None, node.state) 
            if node.parent_node != None:
                self.parent_node = node.parent_node
            self.child_array = [] 
            for x in node.child_array:
                self.child_array.append(new node(None, x))
        else:
            self.state = new state()
            self.parent_node = None
            self.child_array = []

#used to create nodes
class Tree:
    def __init__(self, new_node):
        if new_node = None:
            self.root = node(None, None)
        else:
            self.root = new_node

def calc_ucb(total_sims, num_wins, num_node_sims):
    if num_node_sims == 0:
        #have to return a huge number so that this unvisited node gets visited at least a little bit 
        return 9223372036854775807
    return (num_wins/num_node_sims) + 1.41 * sqrt(log(total_sims) / num_node_sims)

def find_best_ucb(node):
    parent_visit_count = node.state.visit_count
    #the 1st index will be the UCB value of the 1st child node, 2nd index will be the UCB value of the 2nd child node, etc  
    child_ucb = [] 
    for x in child_array of node:
        child_ucb.append(calc_ucb(parent_visit_count, x.state.num_wins, x.state.visit_count))
    #the indices of child_ucb and child_array match which is why returning the index is important
    return node.child_array[child_ucb.index(max(child_ucb))]

def selection(root_node):
    #starts as root node
    child_node = root_node
    while len(node.child_array) > 0:
        #takes on value of best child node of node that was passed into function
        chiild_node = find_best_ucb(node)
    return node

#all this function does is fill up the child_array function in the node class, unless 
#the node represents a win, loss, or tie 
def expand_node(node_to_expand):
    #this function gets all the possible outcomes from node 
    neighboring_nodes = node.state.compute_neighbors()
    #x represents one of the potential states we can get from the node that was passed in
    #already have neighboring states, only need to convert them into nodes and add them to node_to_expand's child array
    for x in neighboring_nodes:
        temp_node = node(x)
        temp_node.parent_node = node_to_expand
        temp_node.state.player_number = temp_node.state.find_opposite_player()
        node_to_expand.child_array.append(temp_node)
    
#same function as before but need it to be outside of state class as well
def find_opposite_player_2(player):
    if player == 'X':
        return 'Y'
    return 'X'

def random_simulation():
    

def montecarlo(self, board, player):
    #1 represents either X or O and 0 represents the other
    opponent = find_opposite_player_2(player)
    tree = new Tree()
    root_node = tree.root
    root_node.state.board = board #in his code he did new Board(board) instead. I don't know if it matters
    root_node.state.player = opponent 

    now = time.time()
    #I decided to give the while loop 1.5 seconds of allotted time. Once the 1.5 seconds are up the while loop ends
    while ((time.time() - now) < 1.5):
        new_node = selection(root_node)
        
        if new_node.state.board.check_win(player) = IN_PROGRESS:
            #expand_node(new_node) find all children

        #node_to_explore = new_node
        #if node_to_explore has children
            #node_to_explore = new_node.get_random_child()
    
        #result = random_simulation(node_to_explore, opponent)
        #backpropagate(node_to_explore, result) 
    
    #winner = root child with max score
    #return board