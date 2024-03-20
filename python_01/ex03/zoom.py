import matplotlib.pyplot as plt
from load_image import ft_load


def main():

    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return
        print(img)

        img = img[100:500, 450:850, :1]
        print(f"New shape after slicing: {img.shape}", end='')
        print(f" or {img.reshape(400, 400).shape}")
        print(img)
        plt.imshow(img, cmap='gray')
        plt.show()

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as msg:
        print(f"Error: {msg}")


if __name__ == "__main__":
    main()
