# 最大地動加速度資訊，單位gal
class Pga:
    def __init__(self):
        # 垂直向PGA
        self.VComponent = None
        # 南北向PGA
        self.NsComponent = None
        # 東西向PGA
        self.EwComponent = None


# 各測站資訊
class EqStation:
    def __init__(self):
        # 測站名稱
        self.StationName = None
        # 測站代碼
        self.StationCode = None
        # 測站位置經度
        self.StationLon = None
        # 測站位置緯度
        self.StationLat = None
        # 震央距離(單位=公里)
        self.Distance = None
        # 測站方位角(單位 = 度)
        self.Azimuth = None
        # 測站震度值
        self.StationIntensity = None
        # 地震儀波形檔網址
        self.WaveImageURI = None
        # 最大地動加速度資訊
        self.Pga = None
        # 資料來源方式
        self.InfoStatus = None
