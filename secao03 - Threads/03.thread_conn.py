import time
from queue import Queue
from threading import Thread
import colorama


def gerador_dados(queue: Queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado', flush=True)
        time.sleep(2)
        queue.put(i)


def consumidor_dados(queue: Queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Dados {valor * 2} processado', flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush=True)
    queue = Queue()
    th1 = Thread(target=gerador_dados, args=(queue,))
    th2 = Thread(target=consumidor_dados, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()