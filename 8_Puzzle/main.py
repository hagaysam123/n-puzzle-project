import numpy as np

from search_algorithms import BFS
from search_algorithms import IDS
from search_algorithms import A_star


def main():

    input_file = open("input.txt", "r")

    # Read data from input file
    with open("input.txt", "r") as input_file:
        algo_num = int(input_file.readline())
        size = int(input_file.readline())
        start_state = input_file.readline()


    start_state = start_state.split("-")

    for x in range(len(start_state)):
        start_state[x] = int(start_state[x])

    input_file.close()

    # Checks if the size of the board game match with the size of the initial state that is given
    if len(start_state) != np.power(size,2):
        print("The size of the board that you entered does not match the size of the initial state you entered"
              + '\n' + "Please check again your input")
        quit()


    output_file = open("output.txt", "w")

    output_file.write("IM FAT" + '\n')

    output_file.close()

    output_file = open("output.txt", "w")


    """
    algo_soul[0] is the number of explored nodes. I also returned it, 
    Because I wanted to check myself and see that my implementations of all the search algorithms are good,
    and also for more tests.
    For example the number of explored nodes in A* should be lower than the number of explored nodes in BFS.
    """

    if algo_num == 1: #BFS
            algo_soul = BFS(start_state, size)
            if len(algo_soul[0]) == 0:
                output_file.write("The input you gave me is also the goal state" + '\n')

            else:
                output_file.write("BFS Solution is: " + str(algo_soul[0]) + '\n')

    elif algo_num == 2: #IDS
        algo_soul = IDS(start_state, size)
        if len(algo_soul[0]) == 0:
            output_file.write("The input you gave me is also the goal state" + '\n')

        else:
            output_file.write("IDS Solution is: " + str(algo_soul[0]) + '\n')

    elif algo_num == 3: #A*
        algo_soul = A_star(start_state, size)
        if len(algo_soul[0]) == 0:
            output_file.write("The input you gave me is also the goal state" + '\n')

        else:
            output_file.write("A* Solution is: " + str(algo_soul[0]) + '\n')

    else:
        print("You didn't enter an appropriate number in the second line, Please check your input")

    print("Finished Calculating, see the answer in the output file")


main()

