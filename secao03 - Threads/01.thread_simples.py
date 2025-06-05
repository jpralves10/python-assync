import threading
import time


def contar(name:str, number: int):
    for n in range(1, number):
        print(f"{n} {name}...")
        time.sleep(1)


def main():
    # th = threading.Thread(target=contar, args=('elefante', 10))
    th = threading.Thread(target=contar, kwargs={"name": 'elefante', "number": 10})

    th.start()  # add a thread na pool de threads prontas para execução
    print('é possivel realizar outras operações enquanto a thread executa .....')
    print('---#---' * 2)

    th.join()  # aguar aqui enquanto a thread termina a execução

    print('Finalizado!')


if __name__ == '__main__':
    main()