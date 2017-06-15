class Value:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


# (氣象)要素值
class ElementValue:
    def __init__(self, value):
        # 資料值
        self.value = value
        # 資料度量單位
        self.measures = None


# 自訂標籤
class Parameter:
    def __init__(self):
        # 自訂標籤名稱
        self.parameter_name = None
        # 自訂標籤值
        self.parameter_value = None
        # 自訂標籤單位
        self.parameter_unit = None


# 自訂標籤群組
class ParameterSet:
    def __init__(self):
        # 自訂標籤群組名稱
        self.parameter_set_name = None
        # 自訂標籤群組
        self.parameter_set_list = []
        # 自訂標籤
        self.parameter_list = []
