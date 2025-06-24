"""Mystery.py"""
#Framework Basics Class
from Module import FileIO
from Module import LoopErr

class Framework():

    #簡単なファイルIO関係
    EasyFileIO = FileIO.EasyFileIO()

    #-------------------------------------------------------------------
    #コンストラクタ
    #def __init__(self):        

    #-------------------------------------------------------------------
    #フレームワーク実行時に一回だけ最初に実行
    def Start(self):
        return 0

    #毎フレーム実行(returnが0以外ならループする)
    def Update(self):
        return 0
    
    #-------------------------------------------------------------------

    #ループエラーの確認とループフラグ
    def Exit(self, loopCode = LoopErr.Code.Looping):
        return loopCode