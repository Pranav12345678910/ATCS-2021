class node:
    def __init__(self, state):
        self.state = state

class Tree:
    def __init__(self):
        self.root = new node(None)

class state:
    def __init__(self, board):
        self.board = board
class board:
    def __init__(self):



def ucb_value(total_visit, win_score, node_visit):
    if node_visit == 0:
        return really big number (so that the node will get selected)
    return (win_score / node_visit) + 1.41 * sqrt(log(totalVisit) / nodeVisit)

def find_best_ucb(node):
    parent_visit_count = number of times node has been visited
    create the array child_ucb = [] #the 1st index will be the UCB value of the 1st child node, 2nd index will be the UCB value of the 2nd child node, etc  
    for x in child_array of node:
        child_ucb.append(calc_ucb(parent_visit_count, x.state.win_score, number of times child has been visited))
    return node.childarray[max index]

def selection(root_node):
    node = root_node
    while node has children:
        node = find_best_ucb(node)
    return node

def montecarlo(self, board, player):
    #opponent = 1 - player
    #tree = new tree()
    #root_node = tree.root (empty because tree was just created)
    #root_node.state.board = board that was passed in
    #root_node.state.player = opponent (opponent's turn)

    #while (program has time):
        #new_node = selection(root_node)

        #if that new_node.status = IN_PROGRESS:
            #expand_node(new_node) find all children

        #node_to_explore = new_node
        #if node_to_explore has children
            #node_to_explore = new_node.get_random_child()
    
        #result = random_simulation(node_to_explore, opponent)
        #backpropagate(node_to_explore, result) 
    
    #winner = root child with max score
    #return board