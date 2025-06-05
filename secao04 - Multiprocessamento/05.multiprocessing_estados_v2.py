import time
from ctypes import c_bool
from multiprocessing import Process, Value


def func1(valor, status):
    if status.value:
        res = valor.value + 10
        status.value = False
    else:
        res = valor.value + 20
        valor.value = 200
        status.value = True

    print(f'O resultado da função 1 é {res}')  # 120
    time.sleep(0.001)


def func2(valor, status):
    if status.value:
        res = valor.value + 30
        status = False
    else:
        res = valor + 40
        valor.value = 400
        status.value = True

    print(f'O resultado da função 2 é {res}')  # 230
    time.sleep(0.001)


def main():
    valor = Value('i', 100)
    status = Value(c_bool, False)

    p1 = Process(target=func1, args=(valor, status))
    p2 = Process(target=func2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
