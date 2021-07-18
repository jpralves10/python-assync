from multiprocessing import Process, JoinableQueue


def ping(queue):
    queue.put('ping')


def pong(queue):
    msg = queue.get()
    print(f'{msg} -> pong')


def main():
    queue = JoinableQueue()  # duas pontas do cano

    p1 = Process(target=ping, args=(queue, ))
    p2 = Process(target=pong, args=(queue, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()