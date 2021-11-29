import json
from typing import Dict, List
import requests
from system_info_init import os_arch, os_check
from datetime import datetime
from tqdm import tqdm

def __init__():
    global __os_arch__, __os_type__
    __os_type__ = os_check()
    if __os_type__ != 'Windows':
        raise Exception("Not a windows machine")
    __os_arch__ =  os_arch()

__init__()

ga = requests.get("http://127.0.0.1:8000?arch="+__os_arch__).text

a : List[Dict[str, List[str]]] =  json.loads(ga)

inp = input("Enter app name: ").lower().replace(" ", "").replace("_", "")

def find_app(inpu: str):
    for g in a:
        for term in g['terms']:
            if term.replace(" ", "") == inpu:
                return [g['link'], g['terms'][0]]
    return 00
    
find = find_app(inp)
if find == 00:
    print("Not found")
else:
    download = requests.get(find[0], stream=True, allow_redirects=True)
    total_length = int(download.headers.get('content-length'))
    name = find[1]+"_download_"+datetime.now().strftime("%f-%S-%M-%I%p-%d-%m-%Y"+".exe")
    with open(name, "wb") as f:
        for i in tqdm(download.iter_content(chunk_size=1023), total=round(total_length / 1024), unit='MB'):
            if i:
                f.write(i)
    print("Downloaded "+find[1])



