import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match = re.fullmatch(r'(^[0]?[0-9]?|[1]?[0-2]?$)', s)
    if match:
        return s
    else:
        return None


if __name__ == "__main__":
    main()