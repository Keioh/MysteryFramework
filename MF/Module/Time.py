"""Time.py"""

import time

class Timer:

    #カウント開始時間
    startTime = 0.0

    #カウント終了時間
    endTime = 0.0

    #カウントの開始と終了の差
    isTime = 0.0

    #時間計測の開始
    def StartTimer(self):
        self.startTime = time.time()

    #時間計測の終了
    def EndTimer(self):
        self.endTime = time.time()

    #計測開始から終了までの時間の差を得る
    def GetTimer(self):
        self.isTime = self.endTime - self.startTime
        return self.isTime