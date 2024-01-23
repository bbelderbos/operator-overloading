class MyContainer:
    def __init__(self, data: list[int]):
        self.data = data

    def __len__(self) -> int:
        return len(self.data)

my_container = MyContainer([1, 2, 3, 4])
length = len(my_container)  # Calls the __len__ method to get the length
print(length)

