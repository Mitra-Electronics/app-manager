from typing import Literal
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

all : dict = {}
win_32 : list =[]
win_64 : list = []

def all_add(dic: dict):
    all.update(dic)
    win_32.append(dic)
    win_64.append(dic)

def git_scrape():
    g = requests.get("https://git-scm.com/download/win", allow_redirects=True)
    soup = BeautifulSoup(g.content, 'lxml')
    scrape = str(soup.find('a', id="auto-download-link"))
    scrape =scrape.replace("<a href=\"", "").replace("\" id=\"auto-download-link\">Click here to download manually</a>", "")
    all_add({"link":scrape, "terms":["git", "git scm", "git-scm"]})

def vs_code_scrape_win_32():
    win_32.append({"link":"https://code.visualstudio.com/sha/download?build=stable&os=win32-user", "terms":["vs code", "visual studio code", "vs-code", "vs code ide", "vs-code-ide"]})

def vs_code_scrape_win_64():
    win_64.append({"link":"https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user", "terms":["vs code", "visual studio code", "vs-code", "vs code ide", "vs-code-ide"]})

def atom_scrape_win_32():
    win_32.append({"link":"https://atom.io/download/windows_x32", "terms":["atom", "atom-ide", "atom ide"]})

def atom_scrape_win_64():
    win_64.append({"link":"https://atom.io/download/windows_x64", "terms":["atom", "atom-ide", "atom ide"]})

def whatsapp_win_32():
    win_32.append({"link":"https://web.whatsapp.com/desktop/windows/release/ia32/WhatsAppSetup.exe", "terms":["whatsapp", "whatsapp desktop", "whatsapp-desktop",
    "whatsapp app", "whatsapp-app", "whatsapp desktop app", "whatsapp-desktop-app"]})

def whatsapp_win_64():
    win_64.append({"link":"https://web.whatsapp.com/desktop/windows/release/x64/WhatsAppSetup.exe", "terms":["whatsapp", "whatsapp desktop", "whatsapp-desktop", 
    "whatsapp app", "whatsapp-app", "whatsapp desktop app", "whatsapp-desktop-app"]})

app = FastAPI()

@app.on_event("startup")
def main():
    git_scrape()
    vs_code_scrape_win_32()
    vs_code_scrape_win_64()
    atom_scrape_win_32()
    atom_scrape_win_64()
    whatsapp_win_32()
    whatsapp_win_64()
    
@app.get('/')
def main(arch: Literal['64-bit', '32-bit']):
    if arch == '64-bit':
        return win_64
    else:
        return win_32