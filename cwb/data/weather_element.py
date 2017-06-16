class WeatherElement:
    def __init__(self):
        # (氣象)要素名稱
        self.element_name = None
        # (氣象)要素描述
        self.description = None
        # 地點
        self.location_list = []
        # 時間
        self.time_list = []
        # (氣象)要素值
        self.element_value = None
        # 資料值
        self.value = None
        # 自訂標籤
        self.parameter_list = []
        # 自訂標籤群組
        self.parameter_set_list = []
