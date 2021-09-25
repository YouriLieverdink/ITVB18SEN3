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
    random.seed(1)

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


def swap(tour, i, j):
    temp = tour[:i]
    temp = temp + tour[i:j+1][::-1]
    temp = temp + tour[j+1:]
    return temp


def two_opt(cities: FrozenSet[Point]) -> List[Point]:
    # Use the NN algorithm combined with k-opt to find an improved guess of the optimal path.
    tour = nearest_neighbour(cities)
    best, n = tour, len(tour)

    improved, iterations = True, 200

    # Returns the next element in the tour.
    def next(i, v=1): return (i + v) % n

    while improved and iterations > 0:
        # Decrease the iterations.
        iterations -= 1
        improved = False

        # Update the counter.
        for i in range(n):
            # Create the first segment.
            s1 = Segment(best[i], best[next(i)])

            for j in range(n - 3):
                # Create the second segment.
                s2 = Segment(best[next(i + j, 2)], best[next(i + j, 3)])

                # Check whether the 2 segments intersect.
                if do_intersect(s1.p1, s1.p2, s2.p1, s2.p2):
                    # Swap the two cities.
                    attempt = swap(best, best.index(s1.p1), best.index(s2.p1))

                    if length(attempt) < length(best):
                        best, improved = attempt, True

    return best


if __name__ == '__main__':
    # Plot the TSP algorithm.

    # 2788.0 km in 2.0547949999999999 s
    # plot_tsp(brute_force, make_cities(10))

    # 3206.7 km in 0.0000450000000000 s
    # plot_tsp(nearest_neighbour, make_cities(10))

    #
    # plot_tsp(two_opt, make_cities(10))

    # ?
    # plot_tsp(brute_force, make_cities(500))

    # 20548.2 km in 0.0713690000000000 s
    # plot_tsp(nearest_neighbour, make_cities(500))

    #
    plot_tsp(two_opt, make_cities(10))
