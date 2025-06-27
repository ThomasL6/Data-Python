from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def trim(array, x, y, width, height, depth=3):
    """
    Trim an array
    """
    # return array[y:y+width, x:x+height, :depth]
    y_end = y + width
    x_end = x + height
    sliced_array = array[y:y_end, x:x_end, :depth]
    return sliced_array


def main():
    """
    Open an image  andprint some information about it,
    before displaying it after zooming in and rotating.
    """
    try:
        img = ft_load("animal.jpeg")
    except Exception as e:
        raise ValueError(f"The image cannot be load: {e}") from e

    print("The shape of the image is:", img.shape)
    print(img)

    img = trim(img, 450, 100, 400, 400, 1)

    print(f'New shape after slicing:, {img.shape}', end='')
    print(f' or ({img.shape[0]}, {img.shape[1]})')
    print(img)

    img = np.squeeze(img)

    if img.shape[0] < 2 or img.shape[1] < 2:
        raise ValueError("Image to small to rotate")

    img_pil = Image.fromarray(img)
    img_rotated = img_pil.rotate(90, resample=Image.NEAREST, expand=True)
    plt.imshow(img_rotated, cmap='gray')
    plt.savefig("output.png")
    plt.axis()
    plt.show()


if __name__ == "__main__":
    main()
