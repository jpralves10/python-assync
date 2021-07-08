import datetime
import math
from multiprocessing import cpu_count
from threading import Thread


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    quantidade_cores = cpu_count()
    print(f'Realizando o processamento com {quantidade_cores} core(s)')

    inicio = datetime.datetime.now()
    ths = []
    for n in range(1, quantidade_cores + 1):
        ini = 50_000_000 * (n - 1) / quantidade_cores + 1
        fim = 50_000_000 * (n) / quantidade_cores
        print(f'core {n} processando de {ini} até {fim}')
        ths.append(
            Thread(target=computar, kwargs={"fim": fim, "inicio": ini}, daemon=True)
        )
    [th.start() for th in ths]
    [th.join() for th in ths]

    tempo = datetime.datetime.now() - inicio

    print(f"terminou em {tempo.total_seconds():.2f} segundos")


if __name__ == '__main__':
    main()

"""
Terminou em 16.07 segundos
"""
