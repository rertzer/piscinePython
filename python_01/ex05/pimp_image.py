import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array):
    """
    Inverts the color of the image received
    """
    try:
        array = 255 - array
    except Exception as e:
        print(e)
    return array


def ft_red(array):
    """
    Filter the red channel of the image received
    """
    try:
        array = array.copy()
        array[:,:,1:] = 0
    except Exception as e:
        print(e)
    return array


def ft_green(array):
    """
    Filter the green channel of the image received
    """
    try:
        array = array.copy()
        array[:,:,0] = 0
        array[:,:,2] = 0
    except Exception as e:
        print(e)
    return array


def ft_blue(array):
    """
    Filter the blue channel of the image received
    """
    try:
        array = array.copy()
        array[:,:,:2] = 0
    except Exception as e:
        print(e)
    return array


def ft_grey(array):
    """
    Convert to grey the image received
    """
    try:
        array = array.copy()
        array[:,:,0] = array[:,:,1] = array[:,:,2] = np.mean(array, axis=2)
    except Exception as e:
        print(e)
    return array


def main():
    """
    main test for pimp_image
    """
    try:
        array = ft_load("landscape.jpg")
        print(ft_invert.__doc__)

        fig, axs = plt.subplots(3,2)
        axs[0, 0].imshow(array)
        axs[0, 0].set_title("Original")
        axs[0, 0].axis('off')

        axs[0, 1].imshow(ft_invert(array))
        axs[0, 1].set_title("Invert")
        axs[0, 1].axis('off')

        axs[1, 0].imshow(ft_red(array))
        axs[1, 0].set_title("Red")
        axs[1, 0].axis('off')

        axs[1, 1].imshow(ft_green(array))
        axs[1, 1].set_title("Green")
        axs[1, 1].axis('off')

        axs[2, 0].imshow(ft_blue(array))
        axs[2, 0].set_title("Blue")
        axs[2, 0].axis('off')

        axs[2, 1].imshow(ft_grey(array))
        axs[2, 1].set_title("Grey")
        axs[2, 1].axis('off')
        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
