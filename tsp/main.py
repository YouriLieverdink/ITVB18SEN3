import itertools
import random
import string
import time
from typing import FrozenSet, List

import matplotlib.pyplot as plt

from intersect import distance, do_intersect
from models import Point, Segment

# Helper functions.


def length(tour: List[Point]) -> float:
    # Returns the length between the points in the tour.
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))


def make_cities(n, width=1000, height=1000):
    # Make a set of (n) cities where each has random coordinates.
    random.seed(3)

    return frozenset(Point(random.randrange(width), random.randrange(height), string.ascii_uppercase[c % 26]) for c in range(n))


def plot_tour(tour):
    # Plot the tour within a frame.
    points = list(tour) + [tour[0]]

    plt.plot([p.x for p in points], [p.y for p in points], 'bo-')

    for p in points:
        label = f"{p.name}"

        plt.annotate(
            label,
            (p.x, p.y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
        )

    plt.axis('scaled')
    plt.axis('off')
    plt.show()


def plot_tsp(algorithm, cities):
    # Apply the provided algorithm to the cities.

    t0 = time.process_time()
    tour = algorithm(cities)
    t1 = time.process_time()

    print(
        "{} city tour with length {:.1f} in {:.16f} secs for {}"
        .format(len(tour), length(tour), t1 - t0, algorithm.__name__)
    )

    print("Start plotting ...")

    plot_tour(tour)


# Algorithms.


def brute_force(cities: FrozenSet[Point]) -> List[Point]:
    # Use brute force to find the optimal path.
    start = next(iter(cities))
    tours = [
        [start] + list(rest) for rest in itertools.permutations(cities - {start})
    ]

    return min(tours, key=length)


def nearest_neighbour(cities: FrozenSet[Point]) -> List[Point]:
    # Use the NN algorithm to find a guess of the optimal path.
    tour = [next(iter(cities))]

    while diff := cities.difference({*tour}):
        cur = tour.pop()
        tour.extend([cur, min(diff, key=lambda k: distance(cur, k))])

    return tour


def two_opt(cities: FrozenSet[Point]) -> List[Point]:
    # Use the NN algorithm combined with k-opt to find an improved guess of the optimal path.
    tour = nearest_neighbour(cities)
    best, improved, n = tour, True, len(tour)

    while improved:
        improved = False

        # Walk through the possible city combinations.
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                # This combination changes nothing.
                if j - i == 1:
                    continue

                attempt = tour[:]
                # Swap the two cities.
                attempt[i:j] = tour[j-1:i-1:-1]
                # Check whether the route has shortend.
                if length(attempt) < length(best):
                    best, improved = attempt, True

        tour = best

    return best


if __name__ == '__main__':
    # Plot the TSP algorithm.

    # 2788.0 km in 2.0547949999999999 s
    # plot_tsp(brute_force, make_cities(10))

    # 3206.7 km in 0.0000450000000000 s
    # plot_tsp(nearest_neighbour, make_cities(10))

    # 2923.6 km in 0.0003780000000000 s
    # plot_tsp(two_opt, make_cities(10))

    # ?
    # plot_tsp(brute_force, make_cities(500))

    # 20548.2 km in 0.0713690000000000 s
    # plot_tsp(nearest_neighbour, make_cities(500))

    # ?
    plot_tsp(two_opt, make_cities(500))
