from time import time

import requests


def get_file(url: str):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(response):
    filename = response.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://loremflickr.com/320/240'
    for i in range(10):
        write_file(get_file(url))


if __name__ == '__main__':
    t0 = time()
    main()
    print(f'it took {time() - t0} seconds')
