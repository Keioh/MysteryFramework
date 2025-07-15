"""horseRacing.py"""
#競馬データ整理

import requests
from bs4 import BeautifulSoup

class HorseRacingDataMining:

    #urlPathで指定したサイトからHTMLを取得する
    def GetWebSite(self, urlPath):

        webSiteFromHTML = requests.get(urlPath)

        return webSiteFromHTML
    
    #GetWebSite()で得た情報からBeautifulSoupObjectを作成する
    def GetBeautifulSoupObject(self, htmlData):

        #パーサーに"lxml"を用いる
        BeautifulSoupObject = BeautifulSoup(htmlData, "lxml")

        return BeautifulSoupObject