from abc import abstractmethod

import requests


class OpenData:
    def __init__(self, data_id, authorization):
        self.__dataId = data_id
        self.__headers = {"Authorization": authorization}

    @abstractmethod
    def _get_payload(self):
        pass

    def get_response(self):
        url = "http://opendata.cwb.gov.tw/api/v1/rest/datastore/{0}".format(self.__dataId)
        payload = self._get_payload()
        if payload is None:
            return requests.get(url, headers=self.__headers)
        else:
            return requests.get(url, params=payload, headers=self.__headers)
