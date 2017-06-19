# 地震規模標籤
class Magnitude:
    def __init__(self):
        # 規模類型
        self.magnitude_type = None
        # 規模大小
        self.magnitude_value = None


# 地震資訊
class EarthquakeInfo:
    def __init__(self, origin_time, epicenter, depth, magnitude):
        # 發震時間
        self.origin_time = origin_time
        # 震央資料
        self.epicenter = epicenter
        # 震源深度，單位公里
        self.depth = depth
        # 規模資訊，包含規模類型及規模大小
        self.magnitude = magnitude
        # 發布地震參數單位
        self.source = None
