# 分區震度資訊
class ShakingArea:
    def __init__(self):
        # 分區描述
        self.AreaDesc = None
        # 分區名稱
        self.AreaName = None
        # 分區震度
        self.AreaIntensity = None
        # 分區圖示顏色
        self.AreaColor = None
        # 資料來源方式
        self.InfoStatus = None
        # 各地震站資訊
        self.EqStationList = []


# 震度資訊
class Intensity:
    def __init__(self):
        # 分區震度資訊
        self.ShakingAreaList = []


# 地震資訊
class Earthquake:
    def __init__(self, report_type, earthquake_no):
        # 報文種類
        self.ReportType = report_type
        # 地震報告編號
        self.EarthquakeNo = earthquake_no
        # 開放資料公告報號
        self.ReportNo = None
        # 報文內容
        self.ReportContent = None
        # 開放資料燈號
        self.ReportColor = None
        # 開放資料參考網址
        self.Web = None
        # 地震報告圖網址
        self.ReportImageURI = None
        # 等震度圖網址
        self.ShakeMapURI = None
        # 地震報告備註
        self.ReportRemark = None
        # 海嘯備註
        self.TsunamiRemark = None
        # 地震資訊
        self.EarthquakeInfo = None
        # 震度資訊
        self.Intensity = None
