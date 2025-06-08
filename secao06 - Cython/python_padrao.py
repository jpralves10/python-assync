import datetime
import math


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f"terminou em {tempo.total_seconds():.2f} segundos")


if __name__ == '__main__':
    main()

"""
Terminou em 18.05 segundos
"""
