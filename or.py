import operator

class CustomList(list):
    def __init__(self, data):
        super().__init__(data)

    def __or__(self, other):
        if len(self) != len(other):
            raise ValueError("Both lists must have the same length for element-wise OR.")

        result = []
        for item1, item2 in zip(self, other):
            result.append(operator.or_(item1, item2))

        return CustomList(result)

# Example usage:
list1 = CustomList([True, False, False])
list2 = CustomList([False, True, False])

result = list1 | list2  # Calls the __or__ method for element-wise OR

print(result)

