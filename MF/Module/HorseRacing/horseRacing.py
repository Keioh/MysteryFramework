"""horseRacing.py"""
#競馬データ整理

import re

class HorseRacingData:

    #一行の中に存在する単語群(','で分割)
    words = []

    #一行中に分割された単語群を纏めたもの
    lines = []

    #検索単語の指定と検索
    def AttributeInformation(self, textLine:str):

        #line変数に対するstr明示宣言
        line:str

        for line in textLine:

            #単語群をリストに追加
            self.words.append(line.split(','))

        #単語群を一行リストに追加
        self.lines.append(self.words)

        return self.lines