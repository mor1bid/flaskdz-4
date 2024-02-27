import time
from pathlib import *
import urllib.request
import shutil
import threading
import multiprocessing
import asyncio

start_time = time.time()

def download(url, start_time):
    response = urllib.request.urlopen(url)
    urls = url.split('/')
    filename = urls[-1]
    with urllib.request.urlopen(url) as response, open(f"./upload/{filename}", 'wb') as file:
        shutil.copyfileobj(response, file)
    print(f"Downloaded {filename} in {time.time()-start_time:.2f} seconds")

def task1(urls: list[str]):
    start_time = time.time()
    for url in urls:
        download(url, start_time)

def task2(urls: list[str]):
    threads = []
    start_time = time.time()
    for url in urls:
        t = threading.Thread(target=download, args=(url, start_time))
        threads.append(t)
        t.start()

def task3(urls: list[str]):
    processs = []
    start_time = time.time()
    for url in urls:
        p = multiprocessing.Process(target=download, args=(url, start_time))
        processs.append(p)
        p.start()
    for p in processs:
        p.join()

async def task4(urls: list[str]):
    start_time = time.time()
    task41 = asyncio.create_task(even(urls, start_time))
    task42 = asyncio.create_task(odd(urls, start_time))
    await task41
    await task42

async def even(urls: list[str], start_time):
    for i in (i for i,url in enumerate(urls) if i / 2 == 0):
        download(urls[i], start_time)
        await asyncio.sleep(0.5)

async def odd(urls: list[str], start_time):
    for i in (i for i,url in enumerate(urls) if i / 2 != 0):
        download(urls[i], start_time)
        await asyncio.sleep(0.5)

def main():
    Path(Path.cwd() / 'upload').mkdir(exist_ok=True)
    urls = [
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/1/12/Romanov2.png', 
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/0/08/CNCR_Kane_Banner.png', 
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/d/df/Tomahawk_Storm.jpg',
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/9/98/TS_Hammerfest_Base.png',
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/4/4b/Montauk_1.jpg',
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/2/2d/Mastermind.jpg'
    ]
    # task1(urls) #стандартное выполнение
    # task2(urls) #многопоточное
    # task3(urls) #многопроцессорное
    asyncio.run(task4(urls)) #ассинхронное
    print(f"Total time: {time.time()-start_time:.2f} seconds")

if __name__=="__main__":
    main()