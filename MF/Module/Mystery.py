"""Mystery.py"""
#Framework Basics Class
from Module import FileIO
from Module import LoopErr
from Module import Timer

#GUI関係
from Module.GUI import MFGUI

#競馬データ計算
from Module.HorseRacing import horseRacing
from Module.HorseRacing import horseRacingDataMining
from Module.HorseRacing import horseRaingEnum

class Framework():

    #簡単なファイルIO関係
    EasyFileIO = FileIO.EasyFileIO()

    #時間計測関係
    Timer = Timer.Timer()

    #競馬データ整理関係
    HouseRaingDataCode = horseRaingEnum.HorseRaingDataCode #Enum
    HourseRacingData = horseRacing.HorseRacingData() #実データ処理関係
    HourseRacingDataMining = horseRacingDataMining.HorseRacingDataMining()#ウェブサイト取得とデータマイニング関係

    #GUI関係
    MysteryGUI = MFGUI.MysteryGUI()

    #-------------------------------------------------------------------
    #コンストラクタ
    #def __init__(self):        

    #-------------------------------------------------------------------
    #フレームワーク実行時に一回だけ最初に実行
    def Start(self):
        return 0

    #毎フレーム実行(returnがLoopErr.Code.Loopingならループする)
    def Update(self):
        return self.Exit()
    
    #-------------------------------------------------------------------

    #ループエラーの確認とループフラグ
    def Exit(self, loopCode = LoopErr.Code.Looping):
        return loopCode