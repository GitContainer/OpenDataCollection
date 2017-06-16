# 天氣預報因子
from enum import Enum


# 今明36小時天氣預報
class TodayTomorrowThirtySixHours(Enum):
    Wx = "Wx"
    PoP = "PoP"
    CI = "CI"
    MinT = "MinT"
    MaxT = "MaxT"


# 未來 2 天天氣預報
class NextTwoDays(Enum):
    Wx = "Wx"
    PoP = "PoP"
    AT = "AT"
    T = "T"
    RH = "RH"
    CI = "CI"
    WeatherDescription = "WeatherDescription"
    PoP6h = "PoP6h"
    Wind = "Wind"
    Td = "Td"


# 未來 1 週天氣預報
class NextOneWeek(Enum):
    MinCI = "MinCI"
    MaxAT = "MaxAT"
    MaxCI = "MaxCI"
    MinT = "MinT"
    UVI = "UVI"
    MinAT = "MinAT"
    MaxT = "MaxT"
    Wind = "Wind"
    Td = "Td"
    PoP = "PoP"
    T = "T"
    RH = "RH"
    Wx = "Wx"
    WeatherDescription = "WeatherDescription"
