import random
player_win = False  # Track if the player has won
opp_win = False  # Track if the opponent (computer or friend) has won
grid_size = 3
player = 'X'
opponent = 'O'
empty_cell = '_'
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
def how_to_play():
    """
    Display instructions on how to play the game.
    """
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
def print_grid():
    """
    Print the current state of the game grid.
    """
    print('-'*15)
    for i in range(grid_size):
        print(' | ', end='')
        for j in range(grid_size):
            print(grid[i * grid_size + j], end=' | ')
        print()
    print('-'*15)
# Function to display the opponent's move
def opp_grid(opp_move_pos):
    """
    Display the opponent's move and print the game grid.

    Parameters:
    - opp_move_pos (int): The position of the opponent's move.
    """
    print("(O) Computer's move:", opp_move_pos + 1)
    print_grid()
# Function for the computer to make a move
def comp_move():
    """
    Implement the computer's move logic based on the win conditions.
    """
    # If there are two Xs, try to block the player by placing an O
    for i in win_conditions:
        if (grid[i[0]] == opponent and grid[i[1]] == opponent and grid[i[2]] == empty_cell) or (grid[i[1]] == opponent and grid[i[2]] == opponent and grid[i[0]] == empty_cell) or (grid[i[0]] == opponent and grid[i[2]] == opponent and grid[i[1]] == empty_cell):
            for pos in i:
                if(grid[pos]==empty_cell):
                    grid[pos]=opponent
                    opp_grid(pos)
                    return
    # If there are two Os, complete the win
    for i in win_conditions:
        if (grid[i[0]] == player and grid[i[1]] == player and grid[i[2]] == empty_cell) or (grid[i[1]] == player and grid[i[2]] == player and grid[i[0]] == empty_cell) or (grid[i[0]] == player and grid[i[2]] == player and grid[i[1]] == empty_cell):
            for pos in i:
                if(grid[pos]==empty_cell):
                    grid[pos]=opponent
                    opp_grid(pos)
                    return
    # If neither winning nor blocking moves are available, make a random move
    comp_int = random.randint(0, 8)
    while grid[comp_int]!=empty_cell:
        comp_int = random.randint(0, 8)
    grid[comp_int] = opponent
    opp_grid(comp_int)
def check_draw():
    """
    Check if the game has ended in a draw.

    Returns:
    - bool: True if the game is a draw, False otherwise.
    """
    if player_win == False and opp_win == False:
        return empty_cell not in grid
def check_win(current_player):
    """
    Check if the specified player has won the game.

    Parameters:
    - current_player (str): The player to check for a win (either 'X' or 'O').

    Returns:
    - bool: True if the player has won, False otherwise.
    """
    for i in win_conditions:
        if grid[i[0]] == current_player and grid[i[1]] == current_player and grid[i[2]] == current_player:
            return True
# Function for the player to make a move
def manual_move(curr_player):
    """
    Get a move from the player and update the game grid.

    Parameters:
    - curr_player (str): The current player making the move ('X' or 'O').
    """
    while True:
        move_input = input(f'({curr_player}) Enter your move: ')
        if(move_input.isnumeric()):
            move_input = eval(move_input)-1
        else:
            print('⚠ Invalid move. Try again.')
            continue
        if 0 <= move_input and move_input <= 8 and grid[move_input] == empty_cell:
            grid[move_input] = curr_player
            if(curr_player==opponent):
                print_grid()
            break
        else:
            print('⚠ Invalid move. Try again.')
            continue
# Main game loop
while(True):
    # Choose opponent type (friend or computer)
    while(True):
        player_choice = input('Who would you like to play with?\n[1]A friend\t[2]Computer\nUse digits to enter your choice: ')
        if(player_choice=='1'):
            opp_player='friend'
            break
        elif(player_choice=='2'):
            opp_player='computer'
            break
        else:
            print('⚠ Invalid choice. Try again.\n','-'*32,sep='')
            continue
    print_grid()
    # Input loop for the game
    while player_win == False and opp_win == False:
        manual_move(player)
        if check_win(player) == True:
            print_grid()
            print('🎉 (X) You won 🎉')
            break
        if check_draw() == False and player_win == False and opp_win == False:
            print_grid()
            if(opp_player=='computer'):
                comp_move()
            else:
                manual_move(opponent)
            if check_win(opponent) == True:
                if(opp_player=='computer'):
                    print('Computer won!')
                else:
                    print('🎉 (O) You won 🎉')
                break
        if check_draw() == True and player_win == False and opp_win == False:
            print_grid()
            print('It was a draw!')
            break
    play_again_choice = None
    # PLay another game choice.
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
        # Reset game variables before starting a new game
        player_win = False; opp_win = False; grid = ['_', '_', '_', '_', '_', '_', '_', '_', '_']; opp_player = 'computer';
        continue
    else:
        break