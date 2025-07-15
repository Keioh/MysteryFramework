"""horseRacing.py"""
#競馬データ整理

#競馬データコード
from Module.HorseRacing import horseRaingEnum

class HorseRacingData:

    #一行の中に存在する単語群(','で分割)
    words = []

    #一行中に分割された単語群を纏めたもの
    lines = []

    #検索単語の指定と検索(return → textLines:str = [テキストブロックの指定=0][ブロック内の行の指定][行内のワードを指定])
    def AttributeInformation(self, textLine:str):

        #line変数に対するstr明示宣言
        line:str

        for line in textLine:

            #単語群をリストに追加
            self.words.append(line.split(','))

        #単語群を一行リストに追加
        self.lines.append(self.words)

        return self.lines
    
    #検索するワードを指定して、その回数を計測する
    def SearchPair(self, searchWord:str):

        #ディクショナリーを宣言
        dataDict = {}

        #同じ単語のカウント
        wordCount = 0

        line:str
        word:str

        #3重for、改善の余地あり
        for line in self.lines:
            for word in  line:
                for data in word:

                    if data.find(searchWord) != -1:
                        wordCount += 1

        dataDict[searchWord] = wordCount

        return dataDict
    
    #全てのデータ上の単語ごとにカウントを自動で行う
    def AutoAllCounting(self):
        return 0