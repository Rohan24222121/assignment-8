class A:
    def __init__(self, a, b, c):
        self.__a = a  # private member
        self._b = b  # protected member
        self.c = c  # public member

    def display(self):
        print("Class A:")
        print("Private member a:", self.__a)
        print("Protected member b:", self._b)
        print("Public member c:", self.c)


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def display(self):
        print("Class B:")
        print("Protected member b (inherited from A):", self._b)
        print("Public member c (inherited from A):", self.c)


# Creating instances and accessing the members

try:
    objA = A(1, 2, 3)
    objA.display()

    objB = B(4, 5, 6)
    objB.display()

    # Trying to access the private member
    print("Trying to access private member a...")
    print(objA.__a)  # Raises an exception
except Exception as e:
    print("Exception occurred:", e)
