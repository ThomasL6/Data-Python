import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Receives an image as a numpy array and inverts the colors
    """
    result = 255 - array
    print(result)
    return result


def ft_red(array: np.array) -> np.ndarray:
    """
    Receives an image as a numpy array and applys a red filter
    """
    result = array.copy()
    result[:, :, 1] = 0
    result[:, :, 2] = 0
    print(result)
    return result


def ft_green(array: np.array) -> np.ndarray:
    """
    Receives an image as a numpy array and applys a green filter
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    print(result)
    return result


def ft_blue(array: np.array) -> np.ndarray:
    """
    Receives an image as a numpy array and applys a blue filter
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    print(result)
    return result


def ft_grey(array: np.array) -> np.ndarray:
    """
    Receives an image as a numpy array and applys a grey filter
    """
    result = array.copy()
    gray = result.mean(axis=2).astype(np.uint8)
    gray_img = np.stack((gray, gray, gray), axis=2)
    print(gray_img)
    return gray_img
