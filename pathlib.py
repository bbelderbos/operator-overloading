import os

class Path:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __truediv__(self, other):
        new_path = os.path.join(self.path, other.path)
        return self.__class__(new_path)

a = Path("foo")
b = Path("bar")
c = a / b
print(c.path)
