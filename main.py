placeholder = ['1','2','3','4','5','6','7','8','9']
winner = ''

def print_table():
    to_print = ''
    for i in range(9):
        to_print += f" {placeholder[i]}"

        if i != 2 and i!= 5 and i!=8:
            to_print += " | "

        if i == 2 or i== 5 or i==8 :
            print(to_print,end='\n')
            if i == 2 or i== 5:
                print("--------------")
            to_print = ""

print("Below table show the positions of the placements.")
#Print the first table to show the positions
print_table()

def play(position :int,player_mark :str):
    """
    Place the annotation and print the placement in the tic-tac-toe table
    :param position: position where should the mark be place
    :param player_mark: which player's mark
    """
    placeholder[position-1] = player_mark
    print_table()


def check_win():
    """
    Check which player win by checking all the tic-tac-toe possibilities in the table
    :returns: True if there is a winner
    """
    #checking for the horizontal wins
    temp = [0,3,6]
    for t in temp:
        if placeholder[t] == placeholder[t+1] == placeholder[t+2]:
            update_winner(placeholder[t])
            return True
    #checking for the vertical wins
    temp = [0, 1, 2]
    for t in temp:
        i = t+3
        if placeholder[t] == placeholder[t+3] == placeholder[i+3]:
            update_winner(placeholder[t])
            return True
    #Checking for the Two diagonal wins
    if placeholder[0] == placeholder[4] == placeholder[8]:
        update_winner(placeholder[0])
        return True
    if placeholder[2] == placeholder[4] == placeholder[6]:
        update_winner(placeholder[2])
        return True

def update_winner(player):
    """
    Decide which player is winner
    """
    global winner
    if player == player_1:
        winner = 'Player 1'
    else:
        winner = 'Player 2'

player_1 = input("Choose player 1 side: X or O : ").upper()

if player_1 == 'X':
    player_2 = 'O'
else:
    player_2 = 'X'

print(f"Player 1: {player_1} Vs Player 2: {player_2} ")

game_over = False
game_loop = 1
while not game_over:

    try:
        game_loop += 1
        position = int(input("Input player 1 position: eg:2 "))
        play(position, player_1)
        somebody_win = check_win()

        if somebody_win:
            print(f"{winner} is the winner!")
            game_over = True
        elif game_loop < 6:
            position = int(input("Input player 2 position: eg:3 "))
            play(position, player_2)
            somebody_win = check_win()
            if somebody_win:
                print(f"{winner} is the winner!")
                game_over = True

        # decide if it is draw
        if game_loop == 6 and not somebody_win:
            print("Draw!")
            game_over = True
    except ValueError:
        game_loop = 1
        print("Position only accept numeric only!")

