import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from load_csv import load


def main():
    """Displays the country information of France versus Germany."""
    try:
        data = load("population_total.csv").set_index('country')
        data = data.iloc[:, 0:251]
        data_france = data.loc['France']
        data_france = data_france.str.replace('M', '').astype('float')
        data_germany = data.loc['Germany'].str.replace('M', '').astype('float')
        fig, ax = plt.subplots(layout='constrained')
        ax.plot(data_france, label='France')
        ax.plot(data_germany, label='Germany')
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.xaxis.set_major_locator(MultipleLocator(40))
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%dM'))
        ax.set_ylabel("Life expectancy")
        plt.legend(loc='lower right')
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
