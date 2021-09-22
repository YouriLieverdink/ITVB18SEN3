import itertools
import math
import random
import time
from collections import namedtuple
from typing import FrozenSet, List, Set

import matplotlib.pyplot as plt

# based on Peter Norvig's IPython Notebook on the TSP

City = namedtuple('City', 'x y')


def distance(A: City, B: City) -> float:
    # Return the distance between A and B.
    return math.hypot(A.x - B.x, A.y - B.y)


def try_all_tours(cities: Set) -> List[City]:
    # generate and test all possible tours of the cities and choose the shortest tour
    tours = alltours(cities)
    return min(tours, key=tour_length)


def alltours(cities: Set) -> List[List[City]]:
    # return a list of tours (a list of lists), each tour a permutation of cities,
    # and each one starting with the same city
    # note: cities is a set, sets don't support indexing
    start = next(iter(cities))
    return [[start] + list(rest) for rest in itertools.permutations(cities - {start})]


def nearest_neighbour(cities: FrozenSet) -> List[City]:
    # Perform the 'Nearest Neighbour, NN' algorithm.
    city = next(iter(cities))
    tour, seen = [city], {city}

    while cities.difference(seen):
        # Retrieve the current and calculate the closest city.
        cur = tour.pop()
        nex = min(cities.difference(seen), key=lambda k: distance(cur, k))

        # Update the tour and seen.
        tour = tour + [cur, nex]
        seen.add(nex)

    return tour


def tour_length(tour):
    # the total of distances between each pair of consecutive cities in the tour
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


def make_cities(n, width=1000, height=1000):
    # Make a set of (n) cities where each has random coordinates.
    random.seed()

    return frozenset(City(random.randrange(width), random.randrange(height)) for c in range(n))


def plot_tour(tour):
    # Plot the tour within a frame.
    points = list(tour) + [tour[0]]

    plt.plot([p.x for p in points], [p.y for p in points], 'bo-')
    plt.axis('scaled')
    plt.axis('off')
    plt.show()


def plot_tsp(algorithm, cities):
    # Apply the provided algorithm to the cities.

    t0 = time.process_time()
    tour = algorithm(cities)
    t1 = time.process_time()

    print(
        "{} city tour with length {:.1f} in {:.3f} secs for {}"
        .format(len(tour), tour_length(tour), t1 - t0, algorithm.__name__)
    )

    print("Start plotting ...")

    plot_tour(tour)


if __name__ == '__main__':
    # Plot the TSP algorithm.
    # plot_tsp(nearest_neighbour, make_cities(10))  # 0.00004400 seconds
    plot_tsp(nearest_neighbour, make_cities(500))  # 0.06097600 seconds
