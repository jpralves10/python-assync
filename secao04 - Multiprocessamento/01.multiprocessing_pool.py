from multiprocessing import Process, current_process

print(f'1 - Iniciando o processo com nome: {current_process().name}')


def faz_algo(valor):
    print(f'valor = {valor}')


def main():
    pc = Process(target=faz_algo, args=('Passaro', ), name='Processo interno')
    print(f'2 - Iniciando o processo com nome: {pc.name}')

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
