import asyncio

import aiofiles


async def exemplo_arq1():
    name_file = '06-01-texto.txt'
    async with aiofiles.open(name_file) as arquivo:
        conteudo = await arquivo.read()
        await asyncio.sleep(1)
    print(conteudo)


async def exemplo_arq2():
    name_file = '06-01-texto.txt'
    async with aiofiles.open(name_file) as arquivo:
        async for linha in arquivo:
            print(linha)
            await asyncio.sleep(1)


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(exemplo_arq1())
    el.close()


if __name__ == '__main__':
    main()