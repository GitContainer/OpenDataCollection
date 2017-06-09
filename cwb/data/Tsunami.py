# 海嘯警戒分區資訊
class WarningArea:
    def __init__(self):
        # 海嘯警戒分區名稱
        self.AreaName = None
        # 海嘯警戒分區描述
        self.AreaDesc = None
        # 海嘯預估波高
        self.WaveHeight = None
        # 預估海嘯到時
        self.ArrivalTime = None
        # 海嘯警戒分區圖示顏色
        self.AreaColor = None
        # 資料來源方式
        self.InfoStatus = None


# 測站
class TsuStation:
    def __init__(self):
        # 測站代碼
        self.StationCode = None
        # 測站名稱
        self.StationName = None
        # 測站位置經度
        self.StationLon = None
        # 測站位置緯度
        self.StationLat = None
        # 觀測海嘯波高，單位公分
        self.WaveHeight = None
        # 觀測海嘯到時
        self.ArrivalTime = None
        # 資料來源方式
        self.InfoStatus = None


# 警戒區域資訊
class TsunamiWave:
    def __init__(self):
        # 海嘯警戒分區資訊
        self.WarningAreaList = []
        # 各潮位站資訊
        self.TsuStationList = []


# 海嘯資訊
class Tsunami:
    def __init__(self, report_type, tsunami_no, report_no, report_content, earthquake_info):
        # 報文種類
        self.ReportType = report_type
        # 海嘯編號
        self.TsunamiNo = tsunami_no
        # 開放資料公告報號
        self.ReportNo = report_no
        # 報文內容
        self.ReportContent = report_content
        # 開放資料燈號
        self.ReportColor = None
        # 開放資料參考網址
        self.Web = None
        # 地震資訊
        self.EarthquakeInfo = earthquake_info
        # 海嘯警戒資訊
        self.TsunamiWave = None
