
class Point:
    def __init__(self, x: float, y: float, name: str) -> None:
        self.x = x
        self.y = y
        self.name = name

    def __str__(self) -> str:
        return '(x: {}, y: {})'.format(self.x, self.y)


class Segment:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return '(p1: {}, p2: {})'.format(self.p1, self.p2)
