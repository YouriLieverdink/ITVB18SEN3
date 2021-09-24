import math

from models import Point


def distance(p1: Point, p2: Point) -> float:
    # Returns the distance between two given points.
    return math.hypot(p2.x - p1.x, p2.y - p1.y)


def on_segment(p1: Point, p2: Point, q: Point) -> bool:
    # Check whether point q is on line segment (p1, p2).
    delta_x, delta_y = (p2.x - p1.x), (p2.y - p1.y)

    a = delta_y if delta_x == 0 else delta_y / delta_x
    b = p1.y - (a * p1.x)

    on_line = q.y == (a * q.x) + b
    is_between = distance(p1, q) + distance(q, p2) == distance(p1, p2)

    return on_line and is_between


def orientation(p1: Point, p2: Point, q1: Point) -> int:
    # Calculates the orientation of the tuple.
    o = (p2.y - p1.y) * (q1.x - p2.x)
    t = (q1.y - p2.y) * (p2.x - p1.x)

    # 0 - Collinear, 1 - Clockwise, 2 - Counter clockwise
    if o == t:
        return 0

    return 1 if o > t else 2


def do_intersect(p1: Point, p2: Point, q1: Point, q2: Point) -> bool:
    # Checks whether the segments (p1, p2) and (q1, q2) intersect.
    o1, o2 = orientation(p1, p2, q1), orientation(p1, p2, q2)
    o3, o4 = orientation(q1, q2, p1), orientation(q1, q2, p2)

    if ((o1 != o2) and (o3 != o4)):
        return True

    # p1, p2, q1 are collinear and q1 lies on segment p1p2.
    if ((o1 == 0) and on_segment(p1, p2, q1)):
        return True

    # p1, p2, q2 are collinear and q2 lies on segment p1p2.
    if ((o2 == 0) and on_segment(p1, p2, q2)):
        return True

    # q1, q2, p1 are collinear and p1 lies on segment q1q2.
    if ((o3 == 0) and on_segment(q1, q2, p1)):
        return True

    # q1, q2, p2 are collinear and p2 lies on segment q1q2.
    if ((o4 == 0) and on_segment(q1, q2, p2)):
        return True

    # Default.
    return False
