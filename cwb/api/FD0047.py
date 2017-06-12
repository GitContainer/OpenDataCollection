from enum import Enum

from cwb.api.Enum import Format
from cwb.api.OpenData import OpenData


class ElementName(Enum):
    Wx = "Wx"
    PoP = "PoP"
    AT = "AT"
    T = "T"
    RH = "RH"
    CI = "CI"
    WeatherDescription = "WeatherDescription"
    PoP6h = "PoP6h"
    Wind = "Wind"
    Td = "Td"


class FD0047(OpenData):
    def _get_payload(self):
        payload = None

        if self._limit != -1:
            if payload is None:
                payload = {}
            payload["limit"] = self._limit

        if self._offset != 0:
            if payload is None:
                payload = {}
            payload["offset"] = self._offset

        if self._format != Format.json:
            if payload is None:
                payload = {}
            payload["format"] = Format.xml.value

        if self._locationName != self._data_id:
            if payload is None:
                payload = {}
            payload["locationName"] = self._locationName

        if len(self._elementNameList) != 0:
            if payload is None:
                payload = {}
            payload["elementName"] = ",".join(en.value for en in self._elementNameList)

        if len(self._sortList) != 0:
            if payload is None:
                payload = {}
            payload["sort"] = ",".join(s.value for s in self._sortList)

        return payload

    def __init__(self, authorization, location_id):
        self._data_id = "F-D0047-" + location_id
        super(FD0047, self).__init__(self._data_id, authorization)
        self._limit = -1
        self._offset = 0
        self._format = Format.json
        self._locationName = self._data_id
        self._elementNameList = []
        self._sortList = []

    def set_limit(self, limit):
        self._limit = limit

    def set_offset(self, offset):
        self._offset = offset

    def set_format(self, format_enum):
        self._format = format_enum

    def set_location_name(self, location_name):
        self._locationName = location_name

    def add_element_name(self, element_name):
        if element_name not in self._elementNameList:
            self._elementNameList.append(element_name)

    def add_sort(self, sort):
        if sort not in self._sortList:
            self._sortList.append(sort)

    def test_payload(self):
        return self._get_payload()
