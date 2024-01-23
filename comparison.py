from functools import total_ordering

@total_ordering
class CustomClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, CustomClass):
            raise ValueError("Can't compare CustomClass with non-CustomClass")
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, CustomClass):
            raise ValueError("Can't compare CustomClass with non-CustomClass")
        return self.value < other.value



# Example usage:
obj1 = CustomClass(42)
obj2 = CustomClass(30)
obj3 = CustomClass(30)

result1 = obj1 < obj2  # Using the < operator
result2 = obj1 > obj2  # Using the > operator
result3 = obj2 == obj3  # Using the == operator
result4 = obj2 >= obj3

print(result1)  # Output: False
print(result2)  # Output: True
print(result3)  # Output: True

