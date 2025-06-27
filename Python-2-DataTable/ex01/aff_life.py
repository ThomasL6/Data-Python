import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import load_csv


def aff_lif():
    """
    Load life expectancy data from a CSV file and plot it.

    Arguments: None
    Returns: None
    """
    path = 'life_expectancy_years.csv'
    df = load_csv.load(path)

    country = 'France'
    data = df[df['country'] == country]
    data = data.drop(columns=['country'])
    data = data.transpose()
    data.columns = [country]

    years = data.index.astype(int)
    values = data[country].values

    plt.plot(years, values, label=country)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{int(x / 1_000_000)}M'))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
    plt.title('France Life Expectancy Projections')
    plt.show()


if __name__ == '__main__':
    aff_lif()
