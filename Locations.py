# 地點
class Location:
    def __init__(self):
        # 緯度
        self.Lat = None
        # 經度
        self.Lon = None
        # 地點名稱
        self.LocationName = None
        # 地點編號
        self.LocationCode = None
        # 測站編號
        self.StationId = None
        # 地理分區編碼
        self.GeoCode = None
        # 多邊形
        self.Polygon = None
        # 地點類型
        self.LocationType = None
        # 時間
        self.TimeList = []
        # 氣象要素
        self.WeatherElementList = []
        # (氣象)要素值
        self.ElementValue = None
        # 資料值
        self.Value = None
        # 自訂標籤
        self.ParameterList = []
        # 自訂標籤群組
        self.ParameterSetList = []
        # 災害性天氣內容標籤
        self.HazardConditionsList = []


# 地點集合
class Locations:
    def __init__(self):
        # 地點集合名稱
        self.LocationsName = None
        # 地點
        self.LocationList = []
        # 自訂標籤
        self.ParameterList = []
        # 自訂標籤群組
        self.ParameterSetList = []
