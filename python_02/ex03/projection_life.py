import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, FixedLocator
from load_csv import load


def kilo_formatter(d, pos):
    """
    Formats values adding k for 10^3
    """
    if d >= 1000:
        d /= 1000
        return '%dk' % d
    else:
        return '%d' % d


def main():
    """
    Displays the projection of life expectancy of various contries
    in relation to the gross national product of the year 1900.
    """
    try:
        income = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        income = income.set_index('country')
        income = income["1900"]

        life_expectancy = load("life_expectancy_years.csv")
        life_expectancy = life_expectancy.set_index('country')
        life_expectancy = life_expectancy["1900"]

        fig, ax = plt.subplots()
        ax.set_title("1900")
        ax.set_ylabel("Life Expectancy")
        ax.set_xlabel("Gross domestic product")
        ax.set_xscale("log")
        ax.xaxis.set_major_locator(FixedLocator([300, 1000, 10000]))
        ax.set_xlim(300, 11000)
        ax.xaxis.set_major_formatter(FuncFormatter(kilo_formatter))
        ax.scatter(income, life_expectancy)
        plt.show()

        """
        ax.xaxis.set_major_locator(MultipleLocator(40))
        ax.yaxis.set_major_locator(MultipleLocator(20))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%dM'))
        ax.set_ylabel("Life expectancy")
        """
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
