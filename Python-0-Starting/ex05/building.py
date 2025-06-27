from sys import argv
import string


def countCharacters(s):
    """Counts and print the numbers of characters
       Args:
        s (str): The input string to analyze.

       Prints:
        - Total number of characters
        - Number of uppercase letters
        - Number of lowercase letters
        - Number of punctuation marks
        - Number of spaces
        - Number of digits
    """
    print(f"The text contains {len(s)} characters:")

    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    punct = sum(1 for c in s if c in string.punctuation)
    space = sum(1 for c in s if c == ' ')
    digit = sum(1 for c in s if c.isdigit())

    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    """Main function that handles input and calls character counting functions.
       Behavior:
          - If no argument is provided, prompts the user to enter a string.
          - If one argument is provided, uses it as the string to analyze.
          - If more than one argument is provided, raises an AssertionError.
    """
    if len(argv) == 1:
        try:
            s = input("What is the text to count?\n")
        except EOFError:
            return
    elif len(argv) == 2:
        s = argv[1]
    else:
        assert False, "more than one argument is provided"

    countCharacters(s)


if __name__ == "__main__":
    main()
