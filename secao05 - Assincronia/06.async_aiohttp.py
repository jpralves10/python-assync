import asyncio
import aiofiles
import aiohttp
import bs4

async def get_links():
    name_file = '06-02-links.txt'
    links = []
    async with aiofiles.open(name_file) as arquivo:
        async for link in arquivo:
            links.append(link.strip())
    return links


async def get_html(link: str):
    print(f'pegando o HTML do curso {link}')

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status()
            return await resp.text()


def get_title(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    title = soup.select_one('title')
    print(title)
    title = title.text.split('|')[0].strip()
    return title


async def imprimir_titulos():
    links = await get_links()

    tarefas = [asyncio.create_task(get_html(link)) for link in links]

    for tarefa in tarefas:
        html = await tarefa
        title = get_title(html)
        print(f'Curso: {title}')


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(imprimir_titulos())
    el.close()


if __name__ == '__main__':
    main()
