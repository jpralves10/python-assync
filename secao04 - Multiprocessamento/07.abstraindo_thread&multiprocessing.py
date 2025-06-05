import time
# from multiprocessing import Process as Executor
from threading import Thread as Executor


def processar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    executor = Executor(target=processar)
    executor.start()
    executor.join()
