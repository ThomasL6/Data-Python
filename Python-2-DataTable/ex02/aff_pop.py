import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import load_csv


def convert_string_to_number(value):
    """
    Converts a string into a number with a suffix into a floating-point number.
    Parameters:
    value (str): The string to convert with a suffix 'M' or 'B'
    Returns:
    float: The converted number as a float.
    If no suffix is present, the value is simply converted to a float.
    """
    value = value.strip()
    if value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('B'):
        return float(value[:-1]) * 1_000_000_000
    else:
        return float(value)


def aff_pop():
    """
    Displays a graph comparing population projections for two countries based
    on data from a CSV file.
    This function visualizes population projections using data from a CSV file.
    It loads the data using the `load_csv` module.
    Parameters:
    None.
    Returns:
    None. Displays an interactive graph.
    """
    path = 'population_total.csv'
    df = load_csv.load(path)

    country1 = 'France'
    country2 = 'Sweden'

    data1 = df[df['country'] == country1].drop(columns=['country'])
    data2 = df[df['country'] == country2].drop(columns=['country'])

    data1 = data1.transpose()
    data2 = data2.transpose()

    data1.columns = [country1]
    data2.columns = [country2]

    data1.index = data1.index.astype(int)
    data2.index = data2.index.astype(int)

    data1[country1] = data1[country1].apply(convert_string_to_number)
    data2[country2] = data2[country2].apply(convert_string_to_number)

    plt.plot(data1.index, data1[country1], label=country1)
    plt.plot(data2.index, data2[country2], label=country2)

    plt.xlabel('Year')
    plt.ylabel('Population')

    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda x, _: f'{int(x / 1_000_000)}M'))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20_000_000))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(40))

    plt.title('Population Projections')
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    aff_pop()
