from multiprocessing import Process, Value, RLock


def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value + 1


def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value - 1


def realizar_transacoes(saldo, lock):
    pc1 = Process(target=depositar, args=(saldo, lock))
    pc2 = Process(target=sacar, args=(saldo, lock))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = Value('i', 100)
    lock = RLock()
    print(f"saldo inicial: {saldo.value}")  # 100

    for _ in range(100):
        realizar_transacoes(saldo, lock)

    print(f"saldo final: {saldo.value}")  # 100
