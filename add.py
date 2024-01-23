class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: " + type(other).__name__)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage:
v1 = Vector(1, 2)
v2 = Vector(3, 4)

result = v1 + v2  # Calls the __add__ method for vector addition

print(result)  # Output: Vector(4, 6)

