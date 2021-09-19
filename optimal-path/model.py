import random
import heapq
from tkinter.constants import S
import config as cf

# global var
grid = [[0 for x in range(cf.SIZE)] for y in range(cf.SIZE)]


class PriorityQueue:
    # a wrapper around heapq (aka priority queue), a binary min-heap on top of a list
    def __init__(self):
        # create a min heap (as a list)
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    # heap elements are tuples (priority, item)
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    # pop returns the smallest item from the heap
    # i.e. the root element = element (priority, item) with highest priority
    def get(self):
        return heapq.heappop(self.elements)[1]


def bernoulli_trial(app):
    return 1 if random.random() < int(app.prob.get())/10 else 0


def get_grid_value(node):
    # node is a tuple (x, y), grid is a 2D-list [x][y]
    return grid[node[0]][node[1]]


def set_grid_value(node, value):
    # node is a tuple (x, y), grid is a 2D-list [x][y]
    grid[node[0]][node[1]] = value


def search(app, start, goal):
    # Setup
    frontier = PriorityQueue()
    visited = set()
    path = dict()

    # Start
    frontier.put(start, 0)

    while not frontier.empty():
        # Retrieve the node with the least cost.
        node = frontier.get()
        app.plot_node(node, cf.PATH_C)
        visited.add(node)

        if node == goal:
            # The goal has been found.
            app.draw_path(path)
            app.pause()

        for neighbour in neighbours(node):
            # Calculate the cost of the neighbour.
            cost = calculate_cost(node) + calculate_cost(node, neighbour)

            if (neighbour not in visited) or (cost < calculate_cost(node)):
                # The node has not been visited or is now cheaper.

                # Remove from frontier if exists.
                for item in frontier.elements:
                    if (item[1] == neighbour):
                        frontier.elements.remove(item)

                # Add to the frontier.
                frontier.put(neighbour, cost)

                # Update the path
                path[neighbour] = node


def calculate_cost(node1, node2=(0, 0)):
    # Calculates the cost based on the current and the starting node.
    return 1000 - sum([node1[0], node1[1], node2[0], node2[1]])


def neighbours(node):
    # Retrieve the neighbours for the provided node.
    neighbours = []

    if node[0] - 1 >= 0:
        next_node = (node[0] - 1, node[1])
        if get_grid_value(next_node) != 'b':
            neighbours.append(next_node)

    if node[1] + 1 < cf.SIZE:
        next_node = (node[0], node[1] + 1)
        if get_grid_value(next_node) != 'b':
            neighbours.append(next_node)

    if node[0] + 1 < cf.SIZE:
        next_node = (node[0] + 1, node[1])
        if get_grid_value(next_node) != 'b':
            neighbours.append(next_node)

    if node[1] - 1 >= 0:
        next_node = (node[0], node[1] - 1)
        if get_grid_value(next_node) != 'b':
            neighbours.append(next_node)

    return neighbours
