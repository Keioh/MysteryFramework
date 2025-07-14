"""THIS FILE IS STARTING MysteryFramework! python3.12"""
#IMPORT
from Module import Mystery

#MainClass
class MysteryFramework(Mystery.Framework):

    #テキストデータ
    textData:str =[[]]

    #フレームワーク実行時に一回だけ最初に実行
    def Start(self):

        #テキストを一行づつ格納するリスト
        textLine:str = []

        detaCount = {}

        #ファイル読み込み
        textLine = self.EasyFileIO.EasyOpenRead("G:\\競馬AI\\データ抽出１０００件くらい修正版.txt")      

        #テキストを分割したデータを抽出
        self.textData = self.HorseRacingData.AttributeInformation(textLine)
        
        #テキストの出現回数のカウント
        detaCount = self.HorseRacingData.SearchPair("ニホンピロホウオー")

        #ファイル出力
        #self.EasyFileIO.EasyOpenWrite("G:\\競馬AI\\TEST.txt",self.textData[0][1][Mystery.Framework.HouseRaingDataCode.jockey])
        self.EasyFileIO.EasyOpenWrite("G:\\競馬AI\\TEST.txt",detaCount)       

        return 0

    #毎フレーム実行
    def Update(self):
        return self.Exit(Mystery.LoopErr.Code.UnLooping)