class Location:
    def __init__(self):
        self.type = None
        self.location_name = None


# 受影響地區
class AffectedAreas:
    def __init__(self):
        # 地點集合
        self.locations_list = []
        # 地點名稱
        self.location_list = []


# 劇烈天氣資訊
class Info:
    def __init__(self):
        # 紀載資訊語系
        self.language = None
        # 天氣現象
        self.phenomena = None
        # 重要性
        self.significance = None
        # 受影響地區
        self.affected_areas_list = []


# 劇烈天氣集
class Hazards:
    def __init__(self):
        # 劇烈天氣資訊
        self.info_list = []
        # 狀態
        self.status = None
        # 作用期間
        self.valid_time = None
        # 劇烈天氣
        self.hazard_list = []


# 劇烈天氣
class Hazard:
    def __init__(self):
        # 劇烈天氣資訊
        self.info = None


# 劇烈天氣狀態
class HazardConditions:
    def __init__(self):
        # 劇烈天氣集
        self.hazards_list = []
        # 劇烈天氣
        self.hazard_list = []
