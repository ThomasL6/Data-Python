import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """
    Function calculating the bmi result from weight and height
    It takes two list of float or integer as arguments
    Returns a list of float
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    for w, h in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("All elements must be int or float.")
    array_height = np.array(height)
    array_weight = np.array(weight)
    bmi = array_weight / (array_height ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Function checking if the result is superior to the limit.
    It get a list and an integer as arguments
    Returns a list of boolean
    """
    # return ([limit <= value for value in bmi])
    result = []
    for value in bmi:
        if value > limit:
            result.append(True)
        else:
            result.append(False)
    return result
