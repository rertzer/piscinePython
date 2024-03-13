import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import UnidentifiedImageError
from load_image import ft_load


def main():
    print(ft_load("animal.jpeg"))

    try:
        with Image.open("animal.jpeg") as f:
            #img = f.convert("L")
            img = np.array(f)

        img = img[100:500, 450:850, :1]
        print(f"New shape after Transpose: {img.shape} or {img.reshape(400, 400).shape}")
        print(img)
        imgplot = plt.imshow(img, cmap='gray')
        plt.show()

    except IOError as msg:
        print(msg)
    except UnidentifiedImageError as msg:
        print(msg)
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
