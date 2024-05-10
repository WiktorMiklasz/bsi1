
from random import randrange, randint
import numpy as np
from nistrng import *
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
def test_key(key: str):
    print("--- GENERATE KEY ---")
    register = [int(char) for char in list(key)]
    bit_array = np.array(register)
    eligible_battery: dict = check_eligibility_all_battery(bit_array, SP800_22R1A_BATTERY)
    results = run_all_battery(bit_array, eligible_battery, False)
    for result, elapsed_time in results:
        if result.passed:
            print("- PASSED - score: " + str(
                np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(
                elapsed_time) + " ms")
        else:
            print("- FAILED - score: " + str(
                np.round(result.score, 3)) + " - " + result.name + " - elapsed time: " + str(
                elapsed_time) + " ms")

def readFile():
    with open('values.txt', 'r') as file:
        data = file.read().replace('\n', '')
    return data

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = readFile()
    string_bit, length = convert(data)
    key = vernam(30000000091, 40000000003, length)
    test_key(key)
    result = encode(string_bit, key)
    if (string_bit == encode(result, key)):
        print("Klucze zgadzaja sie po odkodowaniu!")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
