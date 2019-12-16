class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Position({self.x}, {self.y})"


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + width
        self.y2 = self.y1 + height

    def contains(self, other):
        return self.x1 <= other.x1 <= other.x2 <= self.x2 and self.y1 <= other.y1 <= other.y2 <= self.y2

    def intersects(self, other):
        return self.x1 <= other.x2 and self.x2 >= other.x1 and \
               self.y1 <= other.y2 and self.y2 >= other.y1

    def __repr__(self):
        return f"Rectangle({self.x1}, {self.y1}, {self.x2}, {self.y2}"
