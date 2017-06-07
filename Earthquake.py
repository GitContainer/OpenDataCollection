class ShakingArea:
    def __init__(self):
        self.AreaDesc = None
        self.AreaName = None
        self.AreaIntensity = None
        self.AreaColor = None
        self.InfoStatus = None
        self.EqStation = None


class Intensity:
    def __init__(self):
        self.ShakingArea = None


class Earthquake:
    def __init__(self):
        self.ReportType = None
        self.EarthquakeNo = None
        self.ReportNo = None
        self.ReportContent = None
        self.ReportColor = None
        self.Web = None
        self.ReportImageURI = None
        self.ShakeMapURI = None
        self.ReportRemark = None
        self.TsunamiRemark = None
        self.EarthquakeInfo = None
        self.Intensity = None
