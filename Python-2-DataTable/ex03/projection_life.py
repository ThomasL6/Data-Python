# import pandas as pd
import matplotlib.pyplot as plt
import load_csv


def income_projection():
    """
    Display life expectancy in relation to the gross national product of
    the year 1900 for each country from two csv files.
    """
    living = load_csv.load('life_expectancy_years.csv')
    gnp = load_csv.load(
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')

    year = '1900'
    x = []
    y = []

    for country in living['country']:
        gnp_row = gnp[gnp['country'] == country]
        living_row = living[living['country'] == country]

        if gnp_row.empty or living_row.empty:
            continue

        try:
            income_val = float(gnp_row[year].values[0])
            life_val = float(living_row[year].values[0])
            if income_val >= 300:  # Start at 300
                x.append(income_val)
                y.append(life_val)
        except ValueError:
            continue

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5, edgecolors='w')
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')

    x_ticks = [300, 1000, 10000]
    x_tick_labels = ['300', '1k', '10k']

    plt.xticks(x_ticks, x_tick_labels)

    plt.xlim(300, 10000)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    income_projection()
