from sys import argv


def main():
    """
    Main function mimics a string of characters in a string with Morse code
    """
    NESTED_MORSE = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',

        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    }
    assert len(argv) == 2, "the arguments are bad"
    assert argv[1].isalnum(), "the arguments are bad"

    text = argv[1].upper()

    morse = ' '.join(NESTED_MORSE[c] for c in text if c in NESTED_MORSE)
    print(morse)


if __name__ == "__main__":
    main()
