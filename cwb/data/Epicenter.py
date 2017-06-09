# 震央資料
class Epicenter:
    def __init__(self, epicenter_lon, epicenter_lat):
        # 震央經度，單位度
        self.EpicenterLon = epicenter_lon
        # 震央緯度，單位度
        self.EpicenterLat = epicenter_lat
        # 震央位置
        self.Location = None
