# 震央資料
class Epicenter:
    def __init__(self, epicenter_lon, epicenter_lat):
        # 震央經度，單位度
        self.epicenter_lon = epicenter_lon
        # 震央緯度，單位度
        self.epicenter_lat = epicenter_lat
        # 震央位置
        self.location = None
