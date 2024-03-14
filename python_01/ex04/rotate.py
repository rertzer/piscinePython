import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        img = ft_load("animal.jpeg")
        img = img.reshape(400, 400)
        img = np.array([[img[i][j] for i in range(len(img))]
                       for j in range(len(img[0]))])
        print(f"New shape after Transpose: {img.shape}")
        print(img)
        plt.imshow(img, cmap='gray')
        plt.show()

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as msg:
        print(f"Error: {msg}")


if __name__ == "__main__":
    main()
