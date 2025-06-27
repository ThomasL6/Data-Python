import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Return the shape of a list of lists, and truncated it from the arguments
    and show the new shape

    Parameters :
    family (list) : list of lists
    start (int)   :start of the slice (included).
    end (int)     : wend of the slice (excluded).

    Return :
    list : A list fitting the slice of the list.

    Exceptions :
    - TypeError if 'family' is not a list of lists,
        or if 'start'/'end' are not integers.
    - ValueError if 'start' et 'end' are invalid.
    """

    if (not isinstance(family, list) or
            not all(isinstance(row, list) for row in family)):
        raise TypeError("Family must be a list of lists")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers.")

    if (start < 0 or end < 0 or start > len(family) or
            end > len(family) or start > end):
        raise ValueError("Invalid range for start and end.")

    arr = np.array(family)
    print("My shape is :", arr.shape)
    new_arr = arr[start:end]
    print("My new shape is :", new_arr.shape)
    return new_arr.tolist()
