import random

def display(board):
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3])
    
def player_input():

    """
    Output = (Player1, Player2) a tuple
    """
    
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1 choose X or O: ").upper()

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1,player2)

def place_marker(board,marker,position):

    board[position] = marker

def win_check(board,marker):
    """
    check rows and columns if player won
    check diagonals if player won
    """
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker) or
    (board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker) or
    (board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker))
         

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    return "Player 2"

def space_check(board,position):
    return board[position] == " "

def is_full(board):

    for i in range(1,10):
        if space_check(board,i): #this will return True if there is empty space on board
            return False #board is not full
    #in case there is no empty space available, board is full
    return True

def player_choice(board):

    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position: (1-9) "))

    return position

def replay():

    choice = input("Play again? Yes or No : ")
    return choice.lower() == "yes"


print("Welcome to Tic Tac Toe")   


while True:
    #Play the Game
    #setup board < who goes first < choose marker

    board = [" "]*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()

    print(turn + " will go first.")

    play_game = input("Ready to play? y or n? ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False

    #Actual game play starts here

    while game_on:

        if turn == "Player 1":
            #Player 1 turn
            
            #display board what it looks like
            display(board)
            
            #Ask player 1 to choose a position to place it's marker
            position = player_choice(board)
            
            #Place the marker on position
            place_marker(board,player1_marker,position)
            
            #check if player 1 won
            if win_check(board,player1_marker):
                display(board)
                print("Congratulations! Player 1 won...")
                game_on = False
                
            #check if there is a tie
            else:
                if is_full(board):
                    display(board)
                    print("It's a Tie ")
                    game_on = False
                else:
                    turn = "Player 2"
            
        else:
            #Player 2 turn
             #display board what it looks like
            display(board)
            
            #Ask player 2 to choose a position to place it's marker
            position = player_choice(board)
            
            #Place the marker on position
            place_marker(board,player2_marker,position)
            
            #check if player 2 won
            if win_check(board,player2_marker):
                display(board)
                print("Congratulations! Player 2 won...")
                game_on = False
                
            #check if there is a tie
            else:
                if is_full(board):
                    display(board)
                    print("It's a Tie ")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break


