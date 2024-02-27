import requests, time, os
from flask import Flask
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pathlib import *
import threading
import urllib.request
import shutil

# app = FastAPI()

# @app.get("./upload")
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

def main():
    Path(Path.cwd() / 'upload').mkdir(exist_ok=True)
    urls = [
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/1/12/Romanov2.png', 
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/0/08/CNCR_Kane_Banner.png', 
        'https://static.wikia.nocookie.net/cnc_gamepedia_en/images/d/df/Tomahawk_Storm.jpg'
    ]
    task1(urls)

if __name__=="__main__":
    main()