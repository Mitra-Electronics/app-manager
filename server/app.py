from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

json_ = {"git":""}

@app.on_event("startup")
def main():
    g = requests.get("https://git-scm.com/download/win", allow_redirects=True)
    soup = BeautifulSoup(g.content, 'lxml')
    scrape = str(soup.find('a', id="auto-download-link"))
    scrape =scrape.replace("<a href=\"", "").replace("\" id=\"auto-download-link\">Click here to download manually</a>", "")
    json_.update({"git":scrape})

    
@app.get('/')
def main():
    return json_