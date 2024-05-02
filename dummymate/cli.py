from dummymate.cowsay import cowsay
from termcolor import colored
import argparse


def cli() -> None:
    parser = argparse.ArgumentParser("CLI you never asked for")
    parser.add_argument("message", type=str, help="message that cow said")
    parser.add_argument(
        "-c", "--color", type=str, default="red", help="please spell correctly"
    )
    args = parser.parse_args()

    message = colored(args.message, args.color)
    print(cowsay(message))


if __name__ == "__main__":
    cli()
