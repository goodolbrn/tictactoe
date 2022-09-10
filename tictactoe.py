import sys, os, socket, functions
# All the neccesary functions for main.py are in this file.

def console():
    user_input = input("\033[1;32;40mTTT-Shell |\033[1;33;40m> ")
    if user_input == 'help':
        print("\033[1;36;40m")
        print("1 ) 'help' - bring up this list of commands")
        print("2 ) 'connect' - connect to a TicTacToe server")
        print("3 ) 'host' - host TicTacToe server on local machine")
        print("4 ) 'clear' - clear console")
        print("5 ) 'exit' - exit TTT")
        print("")
        console()
    elif user_input == 'clear':
        if sys.platform == 'darwin':
            os.system('clear')
            console()
        else:
            os.system('cls') # Assuming no one uses linux (distro or otherwise) and only macos or windows to run this program
    elif user_input == 'connect':
        #join server and start game
        server_ip = ""
        def q(server_ip):
            try:
                server_ip = input("\033[1;36;40mIP Address: ")
            except:
                t = input("didn't work...would you like to try again (Y/N)?")
                if t == "Y":
                    q()
                else:
                    console()
        q(server_ip)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect((server_ip, 20))
        except:
            print("\033[1;31;40mA sockets error occured. Is your IP correct? If so, wait a few minutes and try again.")
        game = [3,4,5,6,7,8,9,10,11]
        def j(server, game):
                p1 = server.recv(256).decode()
                if p1 == "UW":
                    server.close()
                    print("\033[1;32;40m@~~~~You WON!~~~~@")
                    return "b"
                elif p1 == "UL":
                    server.close()
                    print("\033[1;31;40mYou lose.")
                    return "b"
                elif p1 == "AT":
                    print("\033[1;31;40mYour square is already taken. Try again")
                    p2 = functions.question(game)
                    game[p2] = 2
                    server.sendall(str(p2).encode())
                    functions.draw_game(game)
                elif p1 == "DR":
                    server.close()
                    print("\033[1;31;40mDraw. You both are equally bad.")
                    return "b"
                elif game[int(p1)] < 3:
                    server.sendall("AT".encode()) # send a message to the other player that this box has already been taken
                    j(server, game)
                else:
                    game[int(p1)] = 1
                    functions.draw_game(game)
        while True:
            p2 = functions.question(game)
            game[p2] = 2
            server.sendall(bytes(str(p2).encode()))
            functions.draw_game(game)
            print("\033[1;33;40m\n")
            print("Waiting on other player...\n")
            if j(server, game) == "b":
                break
        console()
    elif user_input == 'host':
        #start server and game
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.bind(("localhost", 20))
            server.listen()
        except:
            print("\033[1;31;40mCouldn't host server. Check permissions or try again in a few minutes.")
            console()
        connection, address = server.accept()
        print("Connected to "+str(address)+"!")
        game = [3,4,5,6,7,8,9,10,11]
        def j(connection, game):
                p2 = connection.recv(256).decode()
                if p2 == "AT":
                    print("\033[1;36;40mYour number was wrong. Are one of you cheating?")
                    p1 = functions.question(game)
                    game[p1] = 2
                    connection.send(str(p1).encode())
                    functions.draw_game(game)
                    j(connection, game)
                elif game[int(p2)] < 3:
                    connection.sendall("AT".encode()) # send a message to the other player that this box has already been taken
                    j(connection, game)
                else:
                    game[int(p2)] = 2
                    functions.draw_game(game)
        while True:
            j(connection, game)
            
            if functions.array_check(game) == "Draw":
                connection.sendall("DR".encode())
                connection.close()
                print("\033[2;33;40mDraw. You both are equally bad.")
                break
            elif functions.array_check(game) == "True":
                connection.sendall("UW".encode()) # send a message to the other player saying that they have won
                print("\033[1;31;40mYou lose.")
                connection.close()
                break
            else:
                if functions.array_check(game) == "True":
                    connection.sendall("UL".encode()) # send a message to the other player saying that they have lost
                    print("\033[1;32;40m@~~~~You WON!~~~~@")
                    connection.close()
                    break
                p1 = int(functions.question(game))
                game[int(p1)] = 1
                functions.draw_game(game)
                connection.send(str(p1).encode())
                print("\033[1;33;40m\n")
                print("Waiting on other player...\n")
        console()
    elif user_input == 'exit':
        print("\033[1;34;40mGoodbye!")
        exit()
    else:
        print("")
        print("\033[1;31;40mAre you sure your command is correct? Type 'help' for a list.")
        print("")
        console()

