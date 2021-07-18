import asyncio
import datetime


async def gerar_dados(quantidade: int, dados: asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} de dados ...')

    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.0001)
    print(f'{quantidade} dados gerados com sucesso ...')


async def processar_dados(quantidade: int, dados: asyncio.Queue):
    print(f"Aguarde o procesamento de {quantidade} dados ...")
    processados = 0
    while processados < quantidade:
        data = await dados.get()
        print(data)
        processados += 1
        await asyncio.sleep(0.0001)
    print(f'Foram processados {processados} itens')


async def main():
    total = 5_000
    dados = asyncio.Queue()

    print(f'Computando {total * 2: .2f} dados.')
    await gerar_dados(total, dados)
    await gerar_dados(total, dados)
    await processar_dados(total * 2, dados)


if __name__ == '__main__':
    el = asyncio.get_event_loop()
    el.run_until_complete(main())
    el.close()