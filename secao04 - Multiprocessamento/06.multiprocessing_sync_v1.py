from multiprocessing import Process, Value


def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1


def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1


def realizar_transacoes(saldo):
    pc1 = Process(target=depositar, args=(saldo, ))
    pc2 = Process(target=sacar, args=(saldo, ))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()

if __name__ == '__main__':
    saldo = Value('i', 100)

    print(f"saldo inicial: {saldo.value}")  # 100

    for _ in range(100):
        realizar_transacoes(saldo)

    print(f"saldo final: {saldo.value}")  # -8619
