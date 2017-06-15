# 氣象共用資料資料集
class DataSet:
    def __init__(self):
        # 資料集輔助說明資訊
        self.data_set_info = None
        # 資料內容相關說明
        self.contents = None
        # 劇烈天氣狀態標籤
        self.hazard_conditions = None
        # 地點集合
        self.locations_list = []
        # 地點
        self.location_list = []
        # 時間
        self.time_list = []
        # 氣象要素
        self.weather_element_list = []
        # 自訂標籤
        self.parameter_list = []
        # 自訂標籤群組
        self.parameter_set_list = []
        # 資源索引標籤
        self.resource = None
        # 報告類標籤
        self.report = None
        # 海嘯標籤
        self.tsunami = None
        # 地震資訊
        self.earthquake = None
