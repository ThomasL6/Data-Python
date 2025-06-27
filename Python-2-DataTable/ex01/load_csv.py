import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        Dataset: A pandas DataFrame containing the data from the CSV file.
    """
    if not path.endswith('.csv'):
        raise ValueError("The file must be a CSV file.")
    if not isinstance(path, str):  # Ensure path is a string
        raise TypeError("The path must be a string.")
    if not path:   # Ensure path is not empty
        raise ValueError("The path cannot be an empty string.")
    if not pd.io.common.file_exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")
    return pd.read_csv(path)
