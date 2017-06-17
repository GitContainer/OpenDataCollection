class Time:
    def __init__(self):
        # 資料觀測時間
        self.obs_time = None
        # 資料開始時間
        self.start_time = None
        # 資料結束時間
        self.end_time = None
        # tau
        self.tau = None
        # 資料時間
        self.data_time = None
        # 資料有效時間
        self.valid_time = None
        # 資料更新時間
        self.update = None
        # 資料發布時間
        self.issue_time = None
        # 地點
        self.location = None
        # 氣象要素
        # self.weather_element = None
        self.weather_element_list = []
        # (氣象)要素值
        self.element_value = None
        # 資料值
        self.value = None
        # 自訂標籤
        self.parameter = None
        # 自訂標籤群組
        self.parameter_set = None
