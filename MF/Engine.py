"""実行環境"""
import App

#フレームワークの作成
MF = App.MysteryFramework()

#ループコードの保存変数
LoopCode = 0

#一度だけの処理
MF.Start()

#ループ処理
while LoopCode == App.Mystery.LoopErr.Code.Looping:
    LoopCode = MF.Update()