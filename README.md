# MysteryFramework
python3を用いた簡単なフレームワーク

App.pyに処理を書いて、Engine.pyで実行

App.pyのMysteryFrameworkクラス内でselfから各種機能にアクセス可能

# ファイル構成
    MysteryFramework
    |-- App.py #実処理を書くファイルまたは、継承する
    |-- Engine.py #pythonで実行するファイル
    |
    |-- Module
       |-- __init__.py
       |-- FileIO.py #ファイル入出力の簡易化機能群
       |-- Looperr.py #MysteryFrameworkにおけるループした際のエラーコードの定義
       |-- Mystery.py #MysteryFrameworkの統括Class
       |-- Timer.py #タイマー機能群
       | 
       |-- HorseRacing
           |-- __init__.py
           |-- horseRacing.py #抽出データの生成と管理
           |-- horseRaingDataMining.py #未実装