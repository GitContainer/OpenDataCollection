# 天氣預報因子、氣象因子
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


# 即時海況-潮位-沿岸潮位站監測資料
class OA0017ElementName(Enum):
    TidalHeight = "潮高"


# 即時海況-海象海溫-浮標站監測資料
class OA0018ElementName(Enum):
    WindDirection = "風向"
    WindAverage = "平均風"
    Cycle = "週期"
    Gust = "陣風"
    AirTemperature = "氣溫"
    AirPressure = "氣壓"
    SeaTemperature = "海溫"
    WavesHigh = "浪高"
    WaveDirection = "波向"


# 即時海況-海溫-浮標站與沿岸潮位站監測資料
class OA0019ElementName(Enum):
    Depth = "深度"
    SeaTemperature = "海溫"


# 潮汐預報-未來1 個月潮汐預報
class FA0021ElementName(Enum):
    TidalDifference = "潮差"
    LunarCalendar = "農曆"
    DayTide = "1日潮汐"
