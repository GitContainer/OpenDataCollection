class Location:
    def __init__(self):
        self.Type = None
        self.LocationName = None


# 受影響地區
class AffectedAreas:
    def __init__(self):
        # 地點集合
        self.LocationsList = []
        # 地點名稱
        self.LocationList = []


# 劇烈天氣資訊
class Info:
    def __init__(self):
        # 紀載資訊語系
        self.Language = None
        # 天氣現象
        self.Phenomena = None
        # 重要性
        self.Significance = None
        # 受影響地區
        self.AffectedAreasList = []


# 劇烈天氣集
class Hazards:
    def __init__(self):
        # 劇烈天氣資訊
        self.InfoList = []
        # 狀態
        self.Status = None
        # 作用期間
        self.ValidTime = None
        # 劇烈天氣
        self.HazardList = []


# 劇烈天氣
class Hazard:
    def __init__(self):
        # 劇烈天氣資訊
        self.Info = None


# 劇烈天氣狀態
class HazardConditions:
    def __init__(self):
        # 劇烈天氣集
        self.HazardsList = []
        # 劇烈天氣
        self.HazardList = []
