# function to draw TicTacToe squares
def draw_game(game):
        values = ["","","","","","","","",""]
        for i in range(9):
                if game[i] == 1:
                        values[i] = "X"
                elif game[i] == 2:
                        values[i] = "O"
                else:
                        values[i] = " "
                        
        print("\n")
        print("\033[1;34;40m\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
        print('\t_____|_____|_____')

        print("\t     |     |")
        print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
        print('\t_____|_____|_____')

        print("\t     |     |")

        print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
        print("\t     |     |")
        print("\n")

# Check the array to see if there is a winner
def array_check(game):
    if game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or game[6] == game[7] == game[8]:
        return "True"
    elif game[0] == game[3] == game[6] or game[1] == game[4] == game[7] or game[2] == game[5] == game[8]:
        return "True"
    elif game[0] == game[4] == game[8] or game[2] == game[4] == game[6]:
        return "True"
    else:
        return "False"
    x = 0
    for i in game:
        x += i
    if x == 14:
        return "Draw"
        
# Ask question about where to put squares
def question(game):
    p = int(input("\033[1;36;40mPlease choose a number (1-9 inclusive) to represent which square you would like to fill: "))-1
    if game[p] < 3:
        print("Can't do that. Try again.")
        p = question(game)
    return p
