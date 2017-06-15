from abc import abstractmethod

import requests

from cwb.api.Enum import Format


class OpenData:
    def __init__(self, authorization, data_id):
        self.__headers = {"Authorization": authorization}
        self.__dataId = data_id
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

    @abstractmethod
    def _get_payload(self):
        pass

    def _get_response(self):
        url = "http://opendata.cwb.gov.tw/api/v1/rest/datastore/{0}".format(self.__dataId)
        payload = self._get_payload()
        if payload is None:
            return requests.get(url, headers=self.__headers)
        else:
            return requests.get(url, params=payload, headers=self.__headers)

    @abstractmethod
    def get_data_set(self):
        pass
