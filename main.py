from csv import reader
import sys

MAESTRO = 0
PODER = 1


def parse(archivo):
    with open(archivo) as f:
        r = reader(f)
        k = int(next(r).pop())
        maestros_aux = [tuple(line) for line in r]
        maestros = [tuple([m, int(p)]) for (m, p) in maestros_aux]
    return k, maestros


def main():
    if len(sys.argv) != 2:
        sys.exit("USAGE: python main.py <path-a-dataset>")
    print(parse(sys.argv[1]))


if __name__ == '__main__':
    main()
