import numpy as np
from PIL import Image
from PIL import UnidentifiedImageError


def ft_load(path: str):
    """
    Load an jpg or jpeg image, print its format and
    its pixels in RGB format.
    """
    try:
        with Image.open(path) as img:
            if not (img.format == "JPEG" or img.format == "JPG"):
                raise AssertionError("bad format: jpg or jpeg expected")
            img_array = np.array(img)
            print(f"The shape of the image is: {img_array.shape}")
            print(img_array)
        return img_array

    except IOError as msg:
        print(msg)
    except UnidentifiedImageError as msg:
        print(msg)
    except AssertionError as msg:
        print(msg)
