import random
import time
from threading import Thread
from typing import List

import colorama


class Conta:

    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


def criar_contas() -> List[Conta]:
    return [Conta(saldo=random.randint(5_000, 10_000)) for _ in range(10)]


def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return
    origem.saldo -= valor
    time.sleep(0.001)
    destino.saldo += valor


def validar_banco(contas: List[Conta], total: int):
    atual = sum(conta.saldo for conta in contas)

    if atual != total:
        print(colorama.Fore.RED + f"ERROR! Balanço inconsistente. BRL {atual:.2f} vs {total:.2f}", flush=True)
    else:
        print(colorama.Fore.GREEN + f"Balanço consistente. BRL {atual:.2f} vs {total:.2f}", flush=True)


def pega_duas_contas(contas: List[Conta]):
    c1 = random.choice(contas)
    c2 = random.choice(contas)

    while c1 == c2:
        c2 = random.choice(contas)

    return c1, c2


def servicos(contas, total):
    for _ in range(1, 1_000):
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(1, 100)
        transferir(c1, c2, valor)
        validar_banco(contas, total)


def main():
    contas = criar_contas()
    total = sum(conta.saldo for conta in contas)
    print('iniciando transferencias...')

    tarefas = [
        Thread(target=servicos, args=(contas, total)),
        Thread(target=servicos, args=(contas, total)),
        Thread(target=servicos, args=(contas, total)),
        Thread(target=servicos, args=(contas, total)),
        Thread(target=servicos, args=(contas, total)),
        Thread(target=servicos, args=(contas, total)),
    ]

    [t.start() for t in tarefas]
    [t.join() for t in tarefas]

    print('transferencias completas.')
    validar_banco(contas, total)


if __name__ == '__main__':
    main()