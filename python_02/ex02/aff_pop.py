import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from load_csv import load


def main():
    try:
        data = load("life_expectancy_years.csv")
        data = data.set_index('country')
        data = data.loc[['France', 'Germany']]
        data = data.iloc[:, 0:251]
        print(data)
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set_title("France Life expectancy Projections")
        ax.set_xlabel("Year")
        ax.xaxis.set_major_locator(MultipleLocator(40))
        ax.set_ylabel("Life expectancy")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
