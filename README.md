Author: Pranay Maheta
Name: TicTacToe 2-player

TicTacToe 2-player is a simple console emulator that allows people to host and join others running the same software on their network and potentially even the world, although settings on your 
modem/router usually prohibit this for security purposes. In order to play, simply run the 'main.py' script (preferably on your terminal emulator than your IDLE for better results). Depending on 
your firewall or security settings you may have to run this script as a root / Administrator user as the script uses port 20 which may be filtered. 

For testing purposes, have one tab executing the 'host' command and another tab that executes the 'connect' tab. When the connect command asks for an IP Address, use 'localhost' or '127.0.0.1' and it should work.

ERROR HANDLING:
If the server cannot host, wait a few minutes later and try again. On MacOS, you MUST run as root and on Windows you can try to run as Administrator if it doesn't work.

If you cannot connect to an external IP, make sure that both of you are on the same network and that their port 20 is open. Try disable the firewall.

Any other errors should be reported.