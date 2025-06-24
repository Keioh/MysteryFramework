"""Mystery.py"""
#Framework Basics Class
from Module import FileIO
from Module import LoopErr
from Module import Timer

class Framework():

    #簡単なファイルIO関係
    EasyFileIO = FileIO.EasyFileIO()

    #時間計測関係
    Timer = Timer.Timer()

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