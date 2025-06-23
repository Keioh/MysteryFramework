"""実行環境"""
import App

MF = App.MysteryFramework()

#一度だけの処理
MF.Start()

#ループ処理
while MF.Update() != 0:
    MF.Update()