from abc import abstractmethod

import requests


class OpenData:
    def __init__(self, authorization, data_id, location_name_list=[], location_name=None):
        self.__headers = {"Authorization": authorization}
        self._data_id = data_id
        self._limit = -1
        self._offset = 0
        # http://opendata.cwb.gov.tw/opendatadoc/MMC/A0021-001.pdf
        self.__location_name_list = location_name_list
        self.__location_name = location_name
        # http://opendata.cwb.gov.tw/opendatadoc/MMC/A0017-001.pdf A0018-001.pdf A0019-001.pdf
        self.__station_id = []
        self._element_name_list = []
        self._sort_list = []

    def set_limit(self, limit):
        self._limit = limit

    def set_offset(self, offset):
        self._offset = offset

    def add_station_id(self, station_id):
        if station_id not in self.__station_id:
            self.__station_id.append(station_id)

    def add_element_name(self, element_name):
        if element_name not in self._element_name_list:
            self._element_name_list.append(element_name)

    def add_sort(self, sort):
        if sort not in self._sort_list:
            self._sort_list.append(sort)

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

        if len(self.__location_name_list) != 0:
            if payload is None:
                payload = {}
            payload["locationName"] = ",".join(self.__location_name_list)

        if self.__location_name is not None:
            if payload is None:
                payload = {}
            payload["locationName"] = self.__location_name

        if len(self.__station_id) != 0:
            if payload is None:
                payload = {}
            payload["stationId"] = ",".join(si for si in self.__station_id)

        if len(self._element_name_list) != 0:
            if payload is None:
                payload = {}
            payload["elementName"] = ",".join(en.value for en in self._element_name_list)

        if len(self._sort_list) != 0:
            if payload is None:
                payload = {}
            payload["sort"] = ",".join(s.value for s in self._sort_list)

        return payload

    @abstractmethod
    def _set_payload(self, payload):
        pass

    def _get_response(self):
        url = "http://opendata.cwb.gov.tw/api/v1/rest/datastore/{0}".format(self._data_id)

        payload = self._get_payload()
        self._set_payload(payload)
        if payload is None:
            return requests.get(url, headers=self.__headers)
        else:
            return requests.get(url, params=payload, headers=self.__headers)

    @abstractmethod
    def get_data_set(self):
        pass

    def get_payload(self):
        payload = self._get_payload()
        self._set_payload(payload)
        return payload
