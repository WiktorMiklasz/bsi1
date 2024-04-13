# This is a sample Python script.
from random import randrange, randint
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def vernam(a, b, size):
    n = a * b
    s = randint(1, n - 1)
    print("Losowe ziarno to", s)
    x = []
    z = []
    x.append((s * s) % n)
    z.append(x[0] % 2)
    print("Wartosc x[0] to", x[0], "Wartosc z[0] to", z[0])
    for i in range(1, size):
        x.append(x[i - 1] * x[i - 1] % n)
        z.append(x[i] % 2)
    return z


def convert(word):
    # printing original string
    print("Slowo startowe : " + str(word))

    # using join() + ord() + format()
    # Converting String to binary
    res = ''.join(format(ord(i), '08b') for i in word)

    # printing result
    print("Po konwersji : " + str(res))
    return str(res), len(res)


def encode(bit, key):
    result = ""
    for i, j in zip(bit, key):
        result += str(int(int(i) != j))
    print("Zakodowany/Zdekodowany wyraz to " + result)
    return result


def readFile():
    f = open("values.txt", "r")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    word = "string"

    string_bit, length = convert(word)
    key = vernam(30000000091, 40000000003, length)
    result = encode(string_bit, key)
    if (string_bit == encode(result, key)):
        print("Klucze zgadzaja sie po odkodowaniu!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
