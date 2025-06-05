from multiprocessing import cpu_count, Pool


def calcular(valor):
    return valor ** 2


def main():
    tamanho_pool = cpu_count() * 2
    print('tamanho Pool', tamanho_pool)

    pool = Pool(processes=tamanho_pool)

    entradas = list(range(1_000_001))
    saidas = pool.map(calcular, entradas)

    print("saidas", saidas)

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()