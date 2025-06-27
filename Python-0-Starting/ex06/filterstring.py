from sys import argv
from ft_filter import ft_filter


def main():
    """
    Main function that filters words in a string by length greater than N.
    Usage: python3 script.py "your string here" N
    """
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    s = argv[1]
    try:
        n = int(argv[2])
    except ValueError:
        print("AssertionError: second argument must be an integer")
        return

    words = list(ft_filter(lambda word: len(word) > n, s.split()))
    print(words)


if __name__ == "__main__":
    main()
