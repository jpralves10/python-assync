import time
from multiprocessing import Process


def func1(valor, status):
    if status:
        res = valor + 10
        status = False
    else:
        res = valor + 20
        valor = 200
        status = True

    print(f'O resultado da função 1 é {res}')  # 120
    time.sleep(0.001)


def func2(valor, status):
    if status:
        res = valor + 30
        status = False
    else:
        res = valor + 40
        valor = 400
        status = True

    print(f'O resultado da função 2 é {res}')  # 140
    time.sleep(0.001)


def main():
    valor = 100
    status = False

    p1 = Process(target=func1, args=(valor, status))
    p2 = Process(target=func2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
