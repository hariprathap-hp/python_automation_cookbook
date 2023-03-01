from delorean import Delorean
from decimal import Decimal


def main():
    d = Delorean()
    d = d.shift('US/Eastern')
    print(d)

if __name__ == "__main__":
    main()