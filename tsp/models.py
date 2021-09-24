
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Segment:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
