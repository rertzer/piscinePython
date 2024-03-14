import numpy as np
import pandas as pd


def load(path: str):
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape}")
        print(f"data type is {type(data)}")
        return data
    except Exception as e:
        print(f"Loading Error: {e}")


def main():
    print(load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
