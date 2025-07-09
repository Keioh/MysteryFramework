"""FileIO.py"""

class EasyFileIO:

    #全行をリストとして読み込む
    def EasyOpenRead(self, filePath):
        
        #取得した全てのテキストデータ
        textLineData = []

        #取得した一行のテキストデータ
        line = []

        #ファイルの読み込み
        file = open(filePath, encoding="utf-8")

        #ファイル末端まで繰り返す
        while line != '':

            line = file.readline()

            #リストにデータを追加
            textLineData.append(line)

        file.close()

        return textLineData
    

    #リストに纏めた文字列をファイルに書き込む
    def EasyOpenWrite(self, filePath, lineList:str):

        file = open(filePath, "w", encoding="utf-8")

        file.writelines(lineList)
        #file.write(lineList)

        file.close()