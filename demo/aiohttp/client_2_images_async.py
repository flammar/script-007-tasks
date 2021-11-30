import asyncio
from time import time

import aiohttp


# https://youtu.be/LO61F07s7gw?t=2570

async def get_file(url: str, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        # write_image(data)


# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)

def write_image(data):
    filename = f'file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def main():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1):
            task = asyncio.create_task(get_file(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main())
    print(f'it took {time() - t0} seconds')
