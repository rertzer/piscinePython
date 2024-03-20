import pandas as pd


def load(path: str):
    """
    Load takes a path as argument, opens the file,
    writes the dimensions of the data set
    and returns it.
    """
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(f"Loading Error: {e}")
