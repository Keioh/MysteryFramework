"""FileIO.py"""

class EasyFileIO:

    #全行をリストとして読み込む
    def EasyOpenRead(self, filePath):
        
        textLineData = []
        line = []

        file = open(filePath, encoding="utf-8")

        while line != '':

            line = file.readline()

            textLineData.append(line)

        file.close()

        return textLineData
    
    
    #リストに纏めた文字列をファイルに書き込む
    def EasyOpenWrite(self, filePath, lineList:str):

        file = open(filePath, "w", encoding="utf-8")

        file.writelines(lineList)
        #file.write(lineList)

        file.close()