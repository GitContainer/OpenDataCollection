class WarningArea:
    def __init__(self):
        self.AreaName = None
        self.AreaDesc = None
        self.WaveHeight = None
        self.ArrivalTime = None
        self.AreaColor = None
        self.InfoStatus = None


class TsuStation:
    def __init__(self):
        self.StationCode = None
        self.StationName = None
        self.StationLon = None
        self.StationLat = None
        self.WaveHeight = None
        self.ArrivalTime = None
        self.InfoStatus = None


class TsunamiWave:
    def __init__(self):
        self.TsuStation = None
        self.WarningArea = None


class Tsunami:
    def __init__(self):
        self.ReportType = None
        self.TsunamiNo = None
        self.ReportNo = None
        self.ReportContent = None
        self.ReportColor = None
        self.Web = None
        self.EarthquakeInfo = None
        self.TsunamiWave = None
