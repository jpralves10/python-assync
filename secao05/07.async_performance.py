import asyncio
import datetime
import math


async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


def main():
    print('Realizando o processamento matemático de forma assíncrona.')

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    # el.run_until_complete(computar(inicio=1, fim=50_000_000))

    tarefa1 = el.create_task(computar(inicio=0 * 10_000_000 + 1, fim=1 * 10_000_000))
    tarefa2 = el.create_task(computar(inicio=1 * 10_000_000 + 1, fim=2 * 10_000_000))
    tarefa3 = el.create_task(computar(inicio=2 * 10_000_000 + 1, fim=3 * 10_000_000))
    tarefa4 = el.create_task(computar(inicio=3 * 10_000_000 + 1, fim=4 * 10_000_000))
    tarefa5 = el.create_task(computar(inicio=4 * 10_000_000 + 1, fim=5 * 10_000_000))

    tarefas_gather = asyncio.gather(tarefa1, tarefa2, tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas_gather)

    tempo = datetime.datetime.now() - inicio

    print(f'terminou em {tempo.total_seconds():.2f} segundos.')


if __name__ == '__main__':
    main()

"""
    Terminou em 17.67
"""
