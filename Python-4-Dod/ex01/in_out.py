def square(x: int | float) -> int | float:
    """Returns the square of the given number."""
    if x < 0:
        raise ValueError("Negative numbers cannot be squared.")
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the result of raising the number to the power of itself."""
    if x < 0:
        raise ValueError("Negative numbers cannot be powered.")
    return x ** x


def outer(x: int | float, function) -> object:
    """Creates a closure that applies a function to a value."""
    value = x
    if not callable(function):
        raise TypeError("The provided function must be callable.")

    def inner() -> int | float:
        nonlocal value
        value = function(value)
        return value
    return inner
