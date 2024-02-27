import time
from pathlib import *
import urllib.request
import shutil
import threading
import multiprocessing
import asyncio
from flask import Flask

app = Flask(__name__)
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

def main(url):
    Path(Path.cwd() / 'upload').mkdir(exist_ok=True)
    urls = []
    urls.append(url)

    # task1(urls) #стандартное выполнение
    # task2(urls) #многопоточное
    # task3(urls) #многопроцессорное
    asyncio.run(task4(urls)) #ассинхронное
    print(f"Total time: {time.time()-start_time:.2f} seconds")

@app.cli.command("add-url")
def addurl():
    print("Введите адрес желаемого файла: ")
    url = input()
    main(url)


if __name__=="__main__":
    # app.run(debug=True)
    main()