import requests
from bs4 import BeautifulSoup

URL="https://learning.edx.org/course/course-v1:MITx+CTL.SC2x+1T2022/block-v1:MITx+CTL.SC2x+1T2022+type@sequential+block@02004077a1b749be873cb24ec69344b8/block-v1:MITx+CTL.SC2x+1T2022+type@vertical+block@9d3cc8c5f2c14c72b9450f79c113e255"
HEADERS={ "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.4.837 Yowser/2.5 Safari/537.36","accept" : "*/*"}


def get_html(url,params=None):
    r = requests.get(url=URL, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup=BeautifulSoup(html, "html.parser")
    print(soup)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print("error")




parse()
