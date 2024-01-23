class MyList:
    def __init__(self, data: list[int]):
        self.data = data

    def __getitem__(self, index: int) -> int:
       return self.data[index]

my_list = MyList([1, 2, 3, 4])
value = my_list[2]  # Calls the __getitem__ method to access element at index 2
print(value)

