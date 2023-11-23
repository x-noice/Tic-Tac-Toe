import random
# Initialize game state variables
player_win = False  # Track if the player has won
opp_win = False  # Track if the opponent (computer or friend) has won
grid_size = 3  # Size of the game grid
player = 'X'  # Player's symbol
opponent = 'O'  # Opponent's symbol
empty = '_'  # Symbol for an empty cell
grid = ['_', '_', '_', '_', '_', '_', '_', '_', '_']  # The game grid
opp_player = 'computer'  # Default opponent is the computer
# Define win conditions for the game
win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#ASCII Texts
htp_text='''
  _   _                  _____        ____  _             
 | | | | _____      __  |_   _|__    |  _ \\| | __ _ _   _ 
 | |_| |/ _ \\ \\ /\\ / /    | |/ _ \\   | |_) | |/ _` | | | |
 |  _  | (_) \\ V  V /     | | (_) |  |  __/| | (_| | |_| |
 |_| |_|\\___/ \\_/\\_/      |_|\\___/   |_|   |_|\\__,_|\\__, |
                                                    |___/ 
'''
tic_tac_toe='''
  _______ _        _______           _______         
 |__   __(_)      |__   __|         |__   __|        
    | |   _  ___     | | __ _  ___     | | ___   ___ 
    | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\
    | |  | | (__     | | (_| | (__     | | (_) |  __/
    |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|
'''
credit ='''
  __  __           _         ____        
 |  \\/  | __ _  __| | ___   | __ ) _   _ 
 | |\\/| |/ _` |/ _` |/ _ \\  |  _ \\| | | |
 | |  | | (_| | (_| |  __/  | |_) | |_| |
 |_|  |_|\\__,_|\\__,_|\\___|  |____/ \\__, |
                                   |___/ 

 __  __     _ __   ___ (_) ___ ___ 
 \\ \\/ /____| '_ \\ / _ \\| |/ __/ _ \\
  >  <_____| | | | (_) | | (_|  __/
 /_/\\_\\    |_| |_|\\___/|_|\\___\\___|
                                                                                                                                                   
https://github.com/x-noice
'''
#How to play guide
def how_to_play():
    print('-'*55)
    print(tic_tac_toe,'\n',credit)
    print('-'*55)
    print(htp_text)
    print('-'*55)
    for i in range(grid_size):
        print(' | ', end='')
        for j in range(grid_size):
            print(i * grid_size + j + 1 , end=' | ')
        print()
    print('-'*55)
    print('• Use numbers as shown in the grid to place your moves.')
    print('-'*55)
how_to_play()
# Function to print the game grid
def print_grid():
    print('-'*15)
    for i in range(grid_size):
        print(' | ', end='')
        for j in range(grid_size):
            print(grid[i * grid_size + j], end=' | ')
        print()
    print('-'*15)
# Function to display the opponent's move
def opp_grid(opp_move_pos):
    if(opp_player=='computer'):
        print("Computer's move:", opp_move_pos + 1)
    print_grid()
# Function for the opponent to make a move
def comp_move():
    # If there are two Xs, try to block the player by placing an O
    for i in win_conditions:
        if (grid[i[0]] == opponent and grid[i[1]] == opponent and grid[i[2]] == empty) or (grid[i[1]] == opponent and grid[i[2]] == opponent and grid[i[0]] == empty) or (grid[i[0]] == opponent and grid[i[2]] == opponent and grid[i[1]] == empty):
            for pos in i:
                if(grid[pos]==empty):
                    grid[pos]=opponent
                    opp_grid(pos)
                    return
    # If there are two Os, complete the win
    for i in win_conditions:
        if (grid[i[0]] == player and grid[i[1]] == player and grid[i[2]] == empty) or (grid[i[1]] == player and grid[i[2]] == player and grid[i[0]] == empty) or (grid[i[0]] == player and grid[i[2]] == player and grid[i[1]] == empty):
            for pos in i:
                if(grid[pos]==empty):
                    grid[pos]=opponent
                    opp_grid(pos)
                    return
    # If neither winning nor blocking moves are available, make a random move
    comp_int = random.randint(0, 8)
    while grid[comp_int]!=empty:
        comp_int = random.randint(0, 8)
    grid[comp_int] = opponent
    opp_grid(comp_int)
# Function to check for a tie
def check_draw():
    if player_win == False and opp_win == False:
        return empty not in grid
# Function to check for a win condition
def check_win(current_player):
    for win_condition in win_conditions:
        if grid[win_condition[0]] == current_player and grid[win_condition[1]] == current_player and grid[win_condition[2]] == current_player:
            return True
# Function for the player to make a move
def manual_move(curr_player):
    while True:
        move_input = input(f'({curr_player}) Enter your move: ')
        if(move_input.isnumeric()):
            move_input = eval(move_input)-1
        else:
            print('⚠ Invalid move. Try again.')
            continue
        if 0 <= move_input and move_input <= 8 and grid[move_input] == empty:
            grid[move_input] = curr_player
            if(curr_player==opponent):
                opp_grid(move_input)
            break
        else:
            print('⚠ Invalid move. Try again.')
            continue
# Initial game grid
while(True):
    player_win = False; opp_win = False; grid_size = 3; player = 'X'; opponent = 'O'; empty = '_'; grid = ['_', '_', '_', '_', '_', '_', '_', '_', '_']; opp_player = 'computer';
    while(True):
        # Choose the opponent (computer or friend) to play with
        plyr_choice = input('Who would you like to play with?\n[1]A friend\t[2]Computer\nUse digits to enter your choice: ')
        if(plyr_choice=='1'):
            opp_player='friend'
            break
        elif(plyr_choice=='2'):
            opp_player='computer'
            break
        else:
            print('⚠ Invalid choice. Try again.')
            continue
    print_grid()
    # Input loop for the game
    while player_win == False and opp_win == False:
        manual_move(player)
        if check_win(player) == True:
            print_grid()
            print('🎉 (X) You won 🎉')
            break
        # If there's no tie and the game is still ongoing, let the opponent make a move
        if check_draw() == False and player_win == False and opp_win == False:
            print_grid()
            if(opp_player=='computer'):
                comp_move()
            else:
                manual_move(opponent)
            # Check if the opponent has won
            if check_win(opponent) == True:
                if(opp_player=='computer'):
                    print('Computer won!')
                else:
                    print('🎉 (O) You won 🎉')
                break
        # If it's a draw and neither the player nor the opponent has won
        if check_draw() == True and player_win == False and opp_win == False:
            print_grid()
            print('It was a draw!')
            break
    # Play again choice
    play_again_choice = None
    while True:
        print('-'*36)
        play_again_choice = input('Would you like to play another game?\n[1]Yes\t[2]No\nEnter your choice: ')
        if(play_again_choice!='1' and play_again_choice!='2'):
            print('⚠ Invalid choice. Try again.')
            continue
        else:
            break
    if(play_again_choice=='1'):
        print('-'*36)
        continue
    else:
        break