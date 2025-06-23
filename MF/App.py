"""THIS FILE IS STARTING MysteryFramework! python3.12"""
#IMPORT
from Module import Mystery

#MainClass
class MysteryFramework(Mystery.Framework):
    
    #フレームワーク実行時に一回だけ最初に実行
    def Start(self):
        return 0

    #毎フレーム実行
    def Update(self):
        return 0