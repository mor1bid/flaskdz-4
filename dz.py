import requests, time, os
from flask import Flask
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import *

app = FastAPI()

@app.get("/upload")
def download(url, start_time):
    urls = url.split('/')
    filename = "/upload/" + urls[-1]
    # return FileResponse(path='url', filename=filename, media_type='multipart/form-data')
    if os.path.exists(filename):
        return FileResponse(path=filename, filename=filename, media_type='multipart/form-data')
    print(f"Downloaded {filename} in {time.time()-start_time:.2f} seconds")

def task1(urls: list[str]):
    start_time = time.time()
    for url in urls:
        download(url, start_time)

def main():
    Path(Path.cwd() / 'upload').mkdir(exist_ok=True)
    urls = [
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/1/12/Romanov2.png'
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/0/08/CNCR_Kane_Banner.png'
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/d/df/Tomahawk_Storm.jpg'
    ]
    task1(urls)

if __name__=="__main__":
    main()