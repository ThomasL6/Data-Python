from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image from the path given and return it in a numpy array
    Args: path(str), path to the image
    Return: np.ndarray, the image as a numpy array
    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        return img_array
    except Exception as e:
        raise ValueError(f"The image cannot be load: {e}") from e
