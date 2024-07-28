"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    no_of_places_filled = 0
    for row in board:
        for column in row:
            if column is not EMPTY:
                no_of_places_filled += 1
    

    if no_of_places_filled % 2 == 0:
        return X
    
    return O
    
        
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    if terminal(board):
        return f"Game Over"
    
    set_of_possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                set_of_possible_actions.add((i,j))
    

    return set_of_possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")
    
    # Create a deep copy
    deep_copy_of_board = copy.deepcopy(board)

    # Get the player
    name_of_player = player(deep_copy_of_board)
    
    # Create and return the resulting board
    deep_copy_of_board[action[0]][action[1]] = name_of_player
    return deep_copy_of_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if game is in progress
    if not terminal(board):
        return None
    
    # Check if we have a winner
    if check_rows(board) or check_columns(board) or check_diagonals(board):
            if player(board) == X:
                return O
            elif player(board) == O:
                return X

    # Check if it is a tie           
    if check_all_filled(board):
        return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if check_rows(board) or check_columns(board) or check_diagonals(board) or check_all_filled(board):
        return True
    
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    
    print(f"Set of all possible actions is {actions(board)}")
    for action in actions(board):
        print(f"The current action is {action}")
        if player(board) == X:
            print(f"Calling minimax (player X) with board that looks like {board}")
            value_of_max_value_board = max_value(board)
            value_of_min_result_board = min_value(result(board, action))
            print(f"The current value of max_value(board) for action{action} is {value_of_max_value_board}")
            print(f"The current value of value_of_min_result_board(board) for action{action} is {value_of_min_result_board}")
            
            if value_of_max_value_board == value_of_min_result_board:
                return action
            
        else:
            print(f"Calling minimax (player O) with board that looks like {board}")
            value_of_min_value_board = min_value(board)
            value_of_max_result_board = max_value(result(board, action))
            print(f"The current value of min_value(board) for action {action} is {value_of_min_value_board}")
            print(f"The current value of value_of_max_result_board(board) for action{action} is {value_of_max_result_board}")
            
            if value_of_min_value_board == value_of_max_result_board:
                return action




###### Helper functions for terminal() #####

def check_rows(board):
    """
    Checks to see if any of the rows return a winner
    """
    for row in board:
        check_row = set(row)
        if len(check_row) == 1 and EMPTY not in check_row:
            return True
        
    return False

def check_columns(board):
    """
    Checks to see if any of the columns return a winner
    """
    for i in range(3):
        check_column = set()
        for row in board:
            check_column.add(row[i])
        if len(check_column) == 1 and EMPTY not in check_column:
            return True
    
    
    return False

def check_diagonals(board):
    """
    Checks to see if any of the diagonals return a winner
    """
    check_left_diagonal = set()
    check_right_diagonal = set()
    for i in range(3):
        for j in range(3):
            if i == j:
                check_left_diagonal.add(board[i][j])
                
            if i + j == 2:
                check_right_diagonal.add(board[i][j])
        
    if len(check_left_diagonal) == 1 and EMPTY not in check_left_diagonal:
        return True
        
    if len(check_right_diagonal) == 1 and EMPTY not in check_right_diagonal:
        return True
    
    return False

def check_all_filled(board):
    for row in board:
        for column in row:
            if column is EMPTY:
                return False
    
    return True
#######################################################

# Helper functions for Minimax()

def max_value(board):
    print(f"Board passed to max_value is {board}")
    v = -math.inf
    if terminal(board):
        print(f"Utility from max_value is {utility(board)}")
        return utility(board)
    
    for action in actions(board):
        print(f"Inside max_value, out of all possible actions {actions(board)}")
        print(f"we are going to perform action {action}")      
        print(f"on a board that looks like {board}")
        print(f"The current value of v that we are working with is {v}")
        v = max(v,min_value(result(board, action)))
    print(f"The value of v from max_value is {v}")
    return v

def min_value(board):
    print(f"Board passed to min_value is {board}")
    v = math.inf
    if terminal(board):
        print(f"Utility from min_value is {utility(board)}")
        return utility(board)
    
    for action in actions(board):
        print(f"Inside min_value, out of all possible actions {actions(board)}")
        print(f"We are going to perform action {action}")
        print(f"on a board that looks like {board}")
        print(f"The current value of v that we are working with is {v}")
        v = min(v, max_value(result(board, action)))
    print(f"The value of v from min_value is {v}")
    return v
