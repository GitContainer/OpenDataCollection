class Value:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


# (氣象)要素值
class ElementValue:
    def __init__(self, value):
        # 資料值
        self.Value = value
        # 資料度量單位
        self.Measures = None


# 自訂標籤
class Parameter:
    def __init__(self):
        # 自訂標籤名稱
        self.ParameterName = None
        # 自訂標籤值
        self.ParameterValue = None
        # 自訂標籤單位
        self.ParameterUnit = None


# 自訂標籤群組
class ParameterSet:
    def __init__(self):
        # 自訂標籤群組名稱
        self.ParameterSetName = None
        # 自訂標籤群組
        self.ParameterSetList = []
        # 自訂標籤
        self.ParameterList = []
