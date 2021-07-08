from multiprocessing import Process


def faz_algo(valor):
    print(f'{valor}')


def main():
    pc = Process(target=faz_algo, args=('Passaro', ))
    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
