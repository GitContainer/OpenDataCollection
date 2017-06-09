# 氣象共用資料資料集
class DataSet:
    def __init__(self):
        # 資料集輔助說明資訊
        self.DataSetInfo = None
        # 資料內容相關說明
        self.Contents = None
        # 劇烈天氣狀態標籤
        self.HazardConditions = None
        # 地點集合
        self.LocationsList = []
        # 地點
        self.LocationList = []
        # 時間
        self.TimeList = []
        # 氣象要素
        self.WeatherElementList = []
        # 自訂標籤
        self.ParameterList = []
        # 自訂標籤群組
        self.ParameterSetList = []
        # 資源索引標籤
        self.Resource = None
        # 報告類標籤
        self.Report = None
        # 海嘯標籤
        self.Tsunami = None
        # 地震資訊
        self.Earthquake = None
