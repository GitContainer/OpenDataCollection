class Time:
    def __init__(self):
        # 資料觀測時間
        self.ObsTime = None
        # 資料開始時間
        self.StartTime = None
        # 資料結束時間
        self.EndTime = None
        # tau
        self.Tau = None
        # 資料時間
        self.DataTime = None
        # 資料有效時間
        self.ValidTime = None
        # 資料更新時間
        self.Update = None
        # 資料發布時間
        self.IssueTime = None
        # 地點
        self.Location = None
        # 氣象要素
        self.WeatherElement = None
        # (氣象)要素值
        self.ElementValue = None
        # 資料值
        self.Value = None
        # 自訂標籤
        self.Parameter = None
        # 自訂標籤群組
        self.ParameterSet = None
