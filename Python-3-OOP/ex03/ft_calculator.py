class calculator:

    def __init__(self, vector: list) -> None:
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, other) -> None:
        """Add a scalar to the current vector."""
        if isinstance(other, (int, float)):
            self.vector = [x + other for x in self.vector]
            print(self.vector)
        else:
            print("Addition only supports scalar values.")

    def __mul__(self, other) -> None:
        """Multiply a scalar to the current vector."""
        if isinstance(other, (int, float)):
            self.vector = [x * other for x in self.vector]
            print(self.vector)
        else:
            print("Multiplication only supports scalar values.")

    def __sub__(self, other) -> None:
        """Subtract a scalar from the current vector."""
        if isinstance(other, (int, float)):
            self.vector = [x - other for x in self.vector]
            print(self.vector)
        else:
            print("Subtraction only supports scalar values.")

    def __truediv__(self, other) -> None:
        """Divide the current vector by a scalar."""
        if isinstance(other, (int, float)):
            if other == 0:
                print("Division by zero is not allowed.")
            else:
                self.vector = [x / other for x in self.vector]
            print(self.vector)
        else:
            print("Division only supports scalar values.")
