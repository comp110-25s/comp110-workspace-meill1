class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Magic method that returns str representation of a Point object"""
        return f"({self.x}, {self.y})"

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        """Magic method to print str representation of a Line object"""
        return f"Line from {self.start} to {self.end}"
        # return f"y = {get_slope(self)}x + b"

    def get_length(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return (x_diffs**2 + y_diffs**2) ** 0.5

    def get_slope(self) -> float:
        x_diffs: float = self.end.x - self.start.x
        y_diffs: float = self.end.y - self.start.y
        return y_diffs / x_diffs


pt: Point = Point(2.0, 1.0)
print(pt)
me: Point = Point(2.0, 1.0)
planet_y: float = 5.0
planet_loc: Point = Point(me.x + 5, planet_y)
path: Line = Line(me, planet_loc)
print(path)
