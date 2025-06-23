"""Mystery.py"""
#Framework Basics

class Framework:   

    #-------------------------------------------------------------------
    #コンストラクタ
    def __init__(self):
        self.isLoop = True

    #-------------------------------------------------------------------
    #フレームワーク実行時に一回だけ最初に実行
    def Start(self):
        return 0

    #毎フレーム実行(未実装)
    def Update(self):
        return 0