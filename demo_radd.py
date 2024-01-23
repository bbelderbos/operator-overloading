class A:
    def __add__(self, other):
        print("add")
    def __radd__(self, other):
        print("radd")


class B:
    pass

a = A()
b = B()

a + b
b + a
