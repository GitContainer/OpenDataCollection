class Value:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


class ElementValue:
    def __init__(self):
        self.Value = None
        self.Measures = None


class Parameter:
    def __init__(self):
        self.ParameterName = None
        self.ParameterValue = None
        self.ParameterUnit = None


class ParameterSet:
    def __init__(self):
        self.ParameterSetName = None
        self.ParameterSet = None
        self.Parameter = None
