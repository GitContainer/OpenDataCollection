# 地點
class Location:
    def __init__(self):
        # 緯度
        self.lat = None
        # 經度
        self.lon = None
        # 地點名稱
        self.location_name = None
        # 地點編號
        self.location_code = None
        # 測站編號
        self.station_id = None
        # 地理分區編碼
        self.geo_code = None
        # 多邊形
        self.polygon = None
        # 地點類型
        self.location_type = None
        # 時間
        self.time_list = []
        # 氣象要素
        self.weather_element_list = []
        # (氣象)要素值
        self.element_value = None
        # 資料值
        self.value = None
        # 自訂標籤
        self.parameter_list = []
        # 自訂標籤群組
        self.parameter_set_list = []
        # 災害性天氣內容標籤
        self.hazard_conditions_list = []


# 地點集合
class Locations:
    def __init__(self):
        # 地點集合名稱
        self.locations_name = None
        # 地點
        self.location_list = []
        # 自訂標籤
        self.parameter_list = []
        # 自訂標籤群組
        self.parameter_set_list = []
