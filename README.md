# Tic-Tac-Toe
This is a classic game of Tic-Tac-Toe, based on the principles of object-oriented programming. 

A gamer is challenged to play against computer trying to get three crosses/nulls in a row (depends on what he chooses).

TicTacToe class is the descendant of Canvas class from tkinter module. 

Game is an object of the TicTacToe class.

The height and width of the window should be 300x300.

The result of the game is illustrated on the screen.

Steps to run the program locally

* Clone the repo
* Run script: pip install -r -requirements.txt
* Start the app: python main.py

Steps to build the game into an executable

* pip install -r -requirements.txt
* pyinstaller 'main.py' --onefile --name 'tic-tac-toe' --clean
