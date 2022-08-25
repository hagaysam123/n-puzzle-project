import sys

import numpy as np
from vertex import Vertex


# First search algorithm : BFS - Breath First Search
def BFS(initialState, n):
    goal_state = generateGoalState(n)

    root = Vertex(initialState, None, None, 0, 0)

    if root.isGoal(goal_state):
        return root.solution()

    open_list = []
    open_list.append(root)

    close_list = []

    while not (len(open_list) == 0):
        current_node = open_list.pop(0)

        # close_list is a list of states (matrix) the represents the board state of the current node.
        close_list.append(current_node.state)

        # discoverChildren is a function that returns a list of all the children of the current node.
        children = current_node.discoverChildren(n)

        for child in children:
            if child.state in close_list or child in open_list:
                children.remove(child)

        for child in children:
            if child.state not in close_list:
                if child.isGoal(goal_state):
                    return child.solution(), len(close_list)
                open_list.append(child)
    return



# Second search algorithm : IDS - Iterative Depth Search
def IDS(initialState, n):
    goal_state = generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)

    depth = 0
    result = None

    # While we didn't find the solution, we will increase the depth in 1
    while result == None:
        result = deepthLimitedDFS(root, goal_state, depth, n)
        depth += 1
    return result

# Assist function - This function is implementing the DFS search algorithm but runs until given depth
def deepthLimitedDFS(start,GoalState,depth,n):
    open_list = []
    open_list.append(start)
    while True:
        if len(open_list) == 0:
            return None
        curr_node = open_list.pop(0)
        if curr_node.isGoal(GoalState):
            return curr_node.solution(), len(open_list)

        # If we didn't reach to the maximum depth, so we can explore more and discover
        # the children of the current node.
        elif curr_node.depth is not depth:
                children = curr_node.discoverChildren(n)
                open_list.extend(children)



# Third search algorithm : A* - using the manhattan distance as the heuristic function.
def A_star(initialState, n):
    goal_state = generateGoalState(n)
    root = Vertex(initialState, None, None, 0, 0)
    if root.isGoal(goal_state):
        return root.solution()

    open_list = []
    open_list.append(root)

    close_list = []

    while len(open_list) > 0:
        result = minHeuristic(open_list)
        curr_node = result[0]
        if curr_node.isGoal(goal_state):
            return curr_node.solution(), len(close_list)
        open_list.pop(result[1])
        close_list.append(curr_node)

        children = curr_node.discoverChildren(n)

        for node in children:
            if node not in close_list:
                newPotentialCost = curr_node.cost + 1
            """
             if the node doesn't exist in the open_list,
             we need to update his cost, his heuristic, his father, 
             and finally add him to the open_list.
            """
            if not isExist(open_list, node, newPotentialCost, n):
                node.cost = newPotentialCost
                node.heuristic = heuristicFunc(node, n)
                node.pai = curr_node
                open_list.append(node)
    return None


"""""
 Assist function - isExist() is an assist function that her purpose is to check if node 
 exist in the open_list and if yes,
 then updates the cost (the cost of the route from the root) if it is necessary, 
 i.e if the new cost of the route (from the root)
 is lower that the cost thar is written in the open_list.
"""""

def isExist(open_list, v, newPotentialCost, n):
    if len(open_list) == 0:
        return False
    flag = False
    for i, node in enumerate(open_list):
        if v == node:
            if newPotentialCost < open_list[i].cost:
                open_list[i].cost = newPotentialCost
                open_list[i].heuristic = heuristicFunc(open_list[i], n)
                open_list[i].pai = v
                flag = True
    return flag

"""
 minHeuristic() is an assist function that her purpose is to return a list which includes the node 
 and his index which has the lowest heuristic from the nodes in the open_list.
"""
def minHeuristic(open_list):
    minH = sys.maxsize
    indexOfMinNode = 0
    for i, node in enumerate(open_list):
        if node.heuristic < minH:
            minH = node.heuristic
            indexOfMinNode = i
    result = [open_list[indexOfMinNode],indexOfMinNode]
    return result

# Function that generates the GoalState according to n(one dimension from the size of the board).
def generateGoalState(n):
    goal_state = []
    for x in range(np.power(n, 2)):
        goal_state.append(x + 1)
    goal_state[np.power(n, 2) - 1] = 0
    return goal_state

"""
Function that calculates the total heuristic value of a given node.
node.g() returns the cost of the route from the root to the current node.
node.h(n) returns the manhattan distance from the state of the current node 
(that is invoking the function) and the goal state.
"""
def heuristicFunc(node, n):
    return node.g() + node.h(n)

