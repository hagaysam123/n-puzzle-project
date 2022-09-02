# n-puzzle-project

Solving the N puzzle problem using Artificial Intelligence algorithms such as BFS, IDS, A*
implemented with python from scratch.

The program will read its input from a single input.txt file. The first line in the file will determine which one
Algorithm to use:
1 for BFS,
2 for IDS
3 for A*

The size of the board will be written in the second line.

In the third line will be written the initial state of the game.

Then to Run the pogram you start main.py .


Output - the program will write into the file called output.txt and it will contain one line in the following format:
A route is described by the series of actions required to get from the starting state to the ending state. The actions are R
(right) L (left), D (down) and U (up).


Example for input.txt:
2
4
1-2-3-4-5-6-7-8-9-10-11-12-13-0-14-15

Example for output.txt (after running main.py):
LL

