from sys import argv


def main():
    assert len(argv) == 2, (
        "more than one argument is provided"
        if len(argv) > 2
        else "no argument is provided"
    )
    assert argv[1].lstrip('-').isdigit(), "argument is not an integer"

    t = int(argv[1])
    if t % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    return 0


if __name__ == '__main__':
    main()
