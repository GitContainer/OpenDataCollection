# 分區震度資訊
class ShakingArea:
    def __init__(self):
        # 分區描述
        self.area_desc = None
        # 分區名稱
        self.area_name = None
        # 分區震度
        self.area_intensity = None
        # 分區圖示顏色
        self.area_color = None
        # 資料來源方式
        self.info_status = None
        # 各地震站資訊
        self.eq_station_list = []


# 震度資訊
class Intensity:
    def __init__(self):
        # 分區震度資訊
        self.shaking_area_list = []


# 地震資訊
class Earthquake:
    def __init__(self, report_type, earthquake_no):
        # 報文種類
        self.report_type = report_type
        # 地震報告編號
        self.earthquake_no = earthquake_no
        # 開放資料公告報號
        self.report_no = None
        # 報文內容
        self.report_content = None
        # 開放資料燈號
        self.report_color = None
        # 開放資料參考網址
        self.web = None
        # 地震報告圖網址
        self.report_image_uri = None
        # 等震度圖網址
        self.shake_map_uri = None
        # 地震報告備註
        self.report_remark = None
        # 海嘯備註
        self.tsunami_remark = None
        # 地震資訊
        self.earthquake_info = None
        # 震度資訊
        self.intensity = None
