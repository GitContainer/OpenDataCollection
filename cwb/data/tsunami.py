# 海嘯警戒分區資訊
class WarningArea:
    def __init__(self):
        # 海嘯警戒分區名稱
        self.area_name = None
        # 海嘯警戒分區描述
        self.area_desc = None
        # 海嘯預估波高
        self.wave_height = None
        # 預估海嘯到時
        self.arrival_time = None
        # 海嘯警戒分區圖示顏色
        self.area_color = None
        # 資料來源方式
        self.info_status = None


# 測站
class TsuStation:
    def __init__(self):
        # 測站代碼
        self.station_code = None
        # 測站名稱
        self.station_name = None
        # 測站位置經度
        self.station_lon = None
        # 測站位置緯度
        self.station_lat = None
        # 觀測海嘯波高，單位公分
        self.wave_height = None
        # 觀測海嘯到時
        self.arrival_time = None
        # 資料來源方式
        self.info_status = None


# 警戒區域資訊
class TsunamiWave:
    def __init__(self):
        # 海嘯警戒分區資訊
        self.warning_area_list = []
        # 各潮位站資訊
        self.tsu_station_list = []


# 海嘯資訊
class Tsunami:
    def __init__(self, report_type, tsunami_no, report_no, report_content, earthquake_info):
        # 報文種類
        self.report_type = report_type
        # 海嘯編號
        self.tsunami_no = tsunami_no
        # 開放資料公告報號
        self.report_no = report_no
        # 報文內容
        self.report_content = report_content
        # 開放資料燈號
        self.report_color = None
        # 開放資料參考網址
        self.web = None
        # 地震資訊
        self.earthquake_info = earthquake_info
        # 海嘯警戒資訊
        self.tsunami_wave = None
