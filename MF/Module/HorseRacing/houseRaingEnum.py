"""houseRaingEnum.py"""

from enum import IntEnum
from enum import auto

#競馬データコード
class HouseRaingDataCode(IntEnum):
    race_id = 0
    place = auto()
    distance = auto()
    course_type = auto()
    baba_condition = auto()
    weather = auto()
    start_time = auto()
    rank = auto()
    frame = auto()
    horse_name = auto()
    jockey = auto()
    popularity = auto()
    odds = auto()
    horse_weight = auto()
    weight_change = auto()
    running_style = auto()
    pay_tan = auto()
    pay_fuku = auto()
    pay_waku = auto()
    pay_uren = auto()
    pay_wide = auto()
    pay_utan = auto()
    pay_sanfuku = auto()
    pay_santan = auto()