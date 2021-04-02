# Multipicar dos numeros sin usar el signo de multiplicar
# Multiply two integer numbers without using the multiply sign
import numpy as np


def multiply(a, b):
    result = 0
    if np.abs(a) and np.abs(b):
        counter = 0
        POSITIVE_A = np.abs(a) == a
        POSITIVE_B = np.abs(b) == b
        if np.abs(a) > np.abs(b):
            max = np.abs(a)
            min = np.abs(b)
        else:
            max = np.abs(b)
            min = np.abs(a)
        while counter < min:
            result = (
                result + max) if POSITIVE_A == POSITIVE_B else (result - max)
            counter += 1
        return result
    else:
        return result


def run():
    print(multiply(int(input('Ingrese el primer número: ')),
                   int(input('Ingrese el segundo número: '))))


if __name__ == '__main__':
    run()
