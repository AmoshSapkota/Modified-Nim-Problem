import sys

# To returns the amount a player win in a state. i.e. multiplying the number of red and blue marble by 2 and 3 respectively
def score(state):
    return 2* state[0] + 3* state[1]

# To return next move from the given state
def next_move(state):
    red_moves = [(0, state[0]-1, state[1])] if state[0] > 0 else []
    blue_moves = [(1, state[0], state[1]-1)] if state[1] > 0 else []
    return red_moves + blue_moves
# To return another player
def another(player):
    return 0 if player == 1 else 1

# Using MinMax with Alpha Beta Pruning where first call to minimax, initialized alpha and beta to negative and positive infinity, respectively.
def minimax(state, player, depth, alpha=float('-inf'), beta=float('inf')):

    if depth == 0 or state[0] == 0 or state[1] == 0:
        return score(state)

    optimal_score = float('-inf') if player == 0 else float('inf')
    for move in next_move(state):
        new_state = (move[1], move[2])
        value = minimax(new_state, another(player), depth - 1, alpha, beta)

        if player == 0:
            optimal_score = max(optimal_score, value)
            alpha = max(alpha, optimal_score)
            if beta <= alpha:
                break
        else:
            optimal_score = min(optimal_score, value)
            beta = min(beta, optimal_score)
            if beta <= alpha:
                break

    return optimal_score


#Playing game where players are computer and human
def game_playing(state, first_player, depth):
    players = ['Computer', 'Human']
    player = first_player
    while state[0] > 0 and state[1] > 0:
        print("Present state:" + str(state))
        if player == 0:
            print("Computer's turn")
            optimal_score = -sys.maxsize
            best_move = None
            # Using the minimax function, the present move becomes the new best move if its score is higher than the score for the previous best move.
            for move in next_move(state):
                new_state = (move[1], move[2])
                value = minimax(new_state, another(player), depth, -sys.maxsize, sys.maxsize)
                if value > optimal_score:
                    optimal_score = value
                    best_move = move
            pile_color = ['red', 'blue'][best_move[0]]
            print("Computer removes 1 marble from {} pile".format(pile_color))
            state = (best_move[1], best_move[2])
       
        else:
            print("Hello! It's human's turn")
            pile = input("Choose a pile from where you want to remove a marble:(red or blue)")
            while (pile == 'red' and state[0] == 0) or (pile == 'blue' and state[1] == 0) or pile not in ['red', 'blue']:
                pile = input("Please choose a valid pile: ")
            state = (state[0] - (pile == 'red'), state[1] - (pile == 'blue'))
        player = another(player)
    print("Game over!")
    print("Final state:" +str(state))
    if state[0] == 0:
        winner = players[another(player)]
    else:
        winner = players[player]
    print(f"{winner} wins with {score(state)} points")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Command line argument is given in format: red_blue_nim.py <num_red> <num_blue> <first_player> <depth>, where depth is optional and first-player is chosen as computer by default if not specified")
        exit() #Program will be terminated if less than three arguments are given, rather than continuing with invalid inputs
   
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    #If first player isn't specified then computer will start game
    if len(sys.argv) < 4 or sys.argv[3] == 'computer':
    	first_player=0
    else:
    	first_player=1
    #Depth can be given as an argument from command line, else it will be infinity
    depth = int(sys.argv[4]) if len(sys.argv) == 5 else float('inf')
   
    state = (num_red, num_blue)
    game_playing(state, first_player, depth)
