from cwb.api.LocationName import LocationName
from cwb.api.OpenData import OpenData


class FD0047(OpenData):
    def _get_payload(self):
        pass

    def __init__(self, authorization, location_name):
        data_id = "F-D0047-"
        if location_name == LocationName.YilanCounty:
            data_id += "001"

        super(FD0047, self).__init__(data_id, authorization)
        # self._limit = -1
        # self._offset = 0
        # self._format = Format.json
        # self._locationNameList = []
        # self._elementNameList = []
        # self._sortList = []
