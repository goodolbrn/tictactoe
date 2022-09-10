# TicTacToe 2-player text-based Game
# Author: Pranay Maheta
# License: Open source

import tictactoe

screen_width = 100
screen_height = 10

print("\033[1;33;40m_"*screen_width)
for i in range(screen_height-1):
	print("|"," "*(screen_width-3),"|")
print("|"," "*int(screen_width/2 - 17), "____________________________"," "*int(screen_width/2 - 16),"|")
print("|"," "*int(screen_width/2 - 17), "|--------TicTacToe---------|"," "*int(screen_width/2 - 16),"|")
print("|","_"*int(screen_width/2 - 17), "| Created by Pranay Maheta |","_"*int(screen_width/2 - 16),"|")

print("")
print("\033[1;35;40mWelcome to TicTacToe, text-edition! Here is a list of commands that you can use: ")
print("\033[1;33;40m1 ) 'help' - bring up this list of commands")
print("2 ) 'connect' - connect to a TicTacToe server")
print("3 ) 'host' - host TicTacToe server on local machine")
print("4 ) 'clear' - clear console")
print("5 ) 'exit' - exit TTT")
print("")
print("\033[1;35;40mAnd its that simple! Start playing.")
print("")
tictactoe.console()
