"""houseRaingEnum.py"""

from enum import Enum

#競馬データコード
class HouseRaingDataCode(Enum):
    race_id = 0
    place = 1
    distance = 2
    course_type = 3
    baba_condition = 4
    weather = 5
    start_time = 6
    rank = 7
    frame = 8
    horse_name = 9
    jockey = 10
    popularity = 11
    odds = 12
    horse_weight = 13
    weight_change = 14
    running_style = 15
    pay_tan = 16
    pay_fuku = 17
    pay_waku = 18
    pay_uren = 19
    pay_wide = 20
    pay_utan = 21
    pay_sanfuku = 22
    pay_santan = 23