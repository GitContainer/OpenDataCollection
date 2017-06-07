class Location:
    def __init__(self):
        self.type = None
        self.locationName = None


class AffectedAreas:
    def __init__(self, location):
        self.Location = location


class Info:
    def __init__(self, affected_areas):
        self.Language = None
        self.Phenomena = None
        self.Significance = None
        self.AffectedAreas = affected_areas


class Hazards:
    def __init__(self, info, valid_time, hazard):
        self.Info = info
        self.Status = None
        self.ValidTime = valid_time
        self.Hazard = hazard


class Hazard:
    def __init__(self, info):
        self.Info = info


class HazardConditions:
    def __init__(self, hazards, hazard):
        self.Hazard = hazard
        self.Hazards = hazards
