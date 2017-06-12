from enum import Enum

from cwb.api.Enum import Format
from cwb.api.OpenData import OpenData


class ElementName(Enum):
    Wx = "Wx"
    PoP = "PoP"
    CI = "CI"
    MinT = "MinT"
    MaxT = "MaxT"


class FC0032(OpenData):
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

        if len(self._locationNameList) != 0:
            if payload is None:
                payload = {}
            payload["locationName"] = ",".join(self._locationNameList)

        if len(self._elementNameList) != 0:
            if payload is None:
                payload = {}
            payload["elementName"] = ",".join(en.value for en in self._elementNameList)

        if len(self._sortList) != 0:
            if payload is None:
                payload = {}
            payload["sort"] = ",".join(s.value for s in self._sortList)

        return payload

    def __init__(self, authorization):
        super(FC0032, self).__init__("F-C0032-001", authorization)
        self._limit = -1
        self._offset = 0
        self._format = Format.json
        self._locationNameList = []
        self._elementNameList = []
        self._sortList = []

    def set_limit(self, limit):
        self._limit = limit

    def set_offset(self, offset):
        self._offset = offset

    def set_format(self, format_enum):
        self._format = format_enum

    def add_location_name(self, location_name):
        if location_name not in self._locationNameList:
            self._locationNameList.append(location_name)

    def add_element_name(self, element_name):
        if element_name not in self._elementNameList:
            self._elementNameList.append(element_name)

    def add_sort(self, sort):
        if sort not in self._sortList:
            self._sortList.append(sort)

    def test_payload(self):
        return self._get_payload()
