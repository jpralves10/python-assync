from multiprocessing import Pipe, Process


def ping(conn):
    conn.send('ping')


def pong(conn):
    msg = conn.recv()
    print(f'{msg} -> pong')


def main():
    conn1, conn2 = Pipe(duplex=True)  # duas pontas do cano

    p1 = Process(target=ping, args=(conn1, ))
    p2 = Process(target=pong, args=(conn2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()