# 地震規模標籤
class Magnitude:
    def __init__(self):
        # 規模類型
        self.MagnitudeType = None
        # 規模大小
        self.MagnitudeValue = None


# 地震資訊
class EarthquakeInfo:
    def __init__(self, origin_time, epicenter, depth, magnitude):
        # 發震時間
        self.OriginTime = origin_time
        # 震央資料
        self.Epicenter = epicenter
        # 震源深度，單位公里
        self.Depth = depth
        # 規模資訊，包含規模類型及規模大小
        self.Magnitude = magnitude
        # 發布地震參數單位
        self.Source = None
