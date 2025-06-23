"""FileIO.py"""

class EasyFileIO:

    #全行をリストとして読み込む
    def EasyOpenRead(self, filePath):

        file = open(filePath)

        line = file.readline()

        file.close()

        return line
    
    #リストに纏めた文字列をファイルに書き込む
    def EasyOpenWrite(self, filePath, lineList):

        file = open(filePath, mode = "w")

        file.writelines(lineList)

        file.close()