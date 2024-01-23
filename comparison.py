from functools import total_ordering

@total_ordering
class CustomClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, CustomClass):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, CustomClass):
            return self.value < other.value
        return NotImplemented

# Example usage:
obj1 = CustomClass(42)
obj2 = CustomClass(30)
obj3 = CustomClass(30)

result1 = obj1 < obj2  # Using the < operator
result2 = obj1 > obj2  # Using the > operator
result3 = obj2 == obj3  # Using the == operator

print(result1)  # Output: False
print(result2)  # Output: True
print(result3)  # Output: True

