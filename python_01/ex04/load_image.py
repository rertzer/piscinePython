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
        img_array = img_array[100:500, 450:850, :1]
        print(f"The shape of image is: {img_array.shape}")
        return img_array

    except IOError as msg:
        print(msg)
    except UnidentifiedImageError as msg:
        print(msg)
    except AssertionError as msg:
        print(msg)


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
