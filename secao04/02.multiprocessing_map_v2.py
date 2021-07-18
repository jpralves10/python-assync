from multiprocessing import cpu_count, Pool, current_process


def calcular(valor):
    return valor ** 2


def imprimir_nome_processo():
    print(f"iniciando o processo com n ome: {current_process().name}")


def main():
    tamanho_pool = cpu_count() * 2
    print('tamanho Pool', tamanho_pool)

    pool = Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(100))
    saidas = pool.map(calcular, entradas)

    print("saidas", saidas)

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
