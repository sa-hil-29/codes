def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

def position_choice():
    lst = ['0','1','2']
    choice = "WRONG"
    within_range = False
    while choice not in lst:
        choice = input("Choose position(0,1,2): ")
        #Digit Check and range check
        if choice not in lst:
            print("Sorry! invalid choice")       
    return int(choice)

def replacement_choice(game_list,position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    lst = ['Y','N']
    choice = "WRONG"
    within_range = False
    while choice not in lst:
        choice = input("Keep playing? (Y or N): ")
        if choice not in lst:
            print("Sorry! I don't understand please choose Y or N")
    if choice == "Y":
        return True
    return False

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    
    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()
    

