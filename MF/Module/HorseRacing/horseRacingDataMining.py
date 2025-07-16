"""horseRacing.py"""
#競馬データ整理

import requests
from bs4 import BeautifulSoup

class HorseRacingDataMining:
    
    header = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/94.0.4606.61 Safari/537.36"
        )
    }

    #urlPathで指定したサイトからHTMLを取得する
    def GetWebSite(self, urlPath):

        #HTMLを取得する
        webSiteFromHTML = requests.get(urlPath,headers=self.header)

        #文字化け対策
        webSiteFromHTML.encoding = webSiteFromHTML.apparent_encoding

        return webSiteFromHTML
    
    #GetWebSite()で得た情報からBeautifulSoupObjectを作成する
    def GetBeautifulSoupObject(self, htmlData):

        #パーサーに"lxml"を用いる
        BeautifulSoupObject = BeautifulSoup(htmlData, "lxml")

        return BeautifulSoupObject