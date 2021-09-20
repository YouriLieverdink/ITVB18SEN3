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
    # Search the goal using the UCS or A* algorithm.
    frontier = PriorityQueue()
    visited = set()
    path = dict()

    # Add the initial node to the queue.
    frontier.put(start, 0)

    while not frontier.empty():
        # Retrieve the node with the highest priority.
        node = frontier.get()
        app.plot_node(node, cf.PATH_C)

        # Check whether the goal has been reached.
        if node == goal:
            app.draw_path(path)
            break

        visited.add(node)

        # Walk through all the neighbours.
        for neighbour in neighbours(node):
            # Check if the neighbour is valid.
            if get_grid_value(neighbour) == 'b':
                continue

            # Calculate the cost of the neighbour.
            new_cost = get_grid_value(node) + cost(node, neighbour)

            if (neighbour not in visited) or (new_cost < get_grid_value(neighbour)):
                # Update the cost of the neighbour.
                set_grid_value(neighbour, new_cost)

                # Remove from frontier if exists.
                for item in frontier.elements:
                    if (item[1] == neighbour):
                        frontier.elements.remove(item)

                # Calculate the priority.
                priority = new_cost

                if app.alg.get() == 'A*':
                    priority = new_cost + heuristic(neighbour, goal)

                # Add the neighbour to the frontier.
                frontier.put(neighbour, priority)
                visited.add(neighbour)

                # Update the path.
                path[neighbour] = node


def cost(node1, node2):
    # Calculates the cost.
    cost1 = get_grid_value(node1)
    cost2 = get_grid_value(node2)

    if cost2 != -1:
        set_grid_value(node2, cost1 + 1)

    return get_grid_value(node1) + 1


def heuristic(node, goal):
    # Calculates the heuristic based on the current node and goal.
    return sum([goal[0] - node[0], goal[1], node[1]])


def neighbours(node):
    # Retrieve the neighbours for the provided node.
    neighbours = []

    if node[0] - 1 >= 0:
        neighbours.append((node[0] - 1, node[1]))

    if node[1] + 1 < cf.SIZE:
        neighbours.append((node[0], node[1] + 1))

    if node[0] + 1 < cf.SIZE:
        neighbours.append((node[0] + 1, node[1]))

    if node[1] - 1 >= 0:
        neighbours.append((node[0], node[1] - 1))

    return neighbours
