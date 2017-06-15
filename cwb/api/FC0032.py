from cwb.api.Enum import Format
from cwb.api.OpenData import OpenData
from cwb.data.data_set import DataSet
from cwb.data.data_set_info import DataSetInfo
from cwb.data.locations import Location
from cwb.data.parameter_set import Parameter
from cwb.data.time import Time
from cwb.data.WeatherElement import WeatherElement


class FC0032(OpenData):
    def get_data_set(self):
        records = self._get_response().json()["records"]

        data_set_info = DataSetInfo()
        data_set_info.DataSetDescription = records["datasetDescription"]

        data_set = DataSet()
        data_set.DataSetInfo = data_set_info

        for l in records["location"]:
            location = Location()
            location.LocationName = l["locationName"]

            for we in l["weatherElement"]:
                weather_element = WeatherElement()
                weather_element.ElementName = we["elementName"]

                for t in we["time"]:
                    time = Time()
                    time.StartTime = t["startTime"]
                    time.EndTime = t["endTime"]

                    parameter = Parameter()
                    if t["parameter"].get("parameterName", None) is not None:
                        parameter.ParameterName = t["parameter"]["parameterName"]
                    if t["parameter"].get("parameterValue", None) is not None:
                        parameter.ParameterValue = t["parameter"]["parameterValue"]
                    if t["parameter"].get("parameterUnit", None) is not None:
                        parameter.ParameterUnit = t["parameter"]["parameterUnit"]
                    time.Parameter = parameter

                    weather_element.TimeList.append(time)

                location.WeatherElementList.append(weather_element)

            data_set.LocationList.append(location)

        return data_set

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
        super(FC0032, self).__init__(authorization, "F-C0032-001")
        # self._limit = -1
        # self._offset = 0
        # self._format = Format.json
        # self._locationNameList = []
        # self._elementNameList = []
        # self._sortList = []

    # def set_limit(self, limit):
    #     self._limit = limit
    #
    # def set_offset(self, offset):
    #     self._offset = offset
    #
    # def set_format(self, format_enum):
    #     self._format = format_enum
    #
    # def add_location_name(self, location_name):
    #     if location_name not in self._locationNameList:
    #         self._locationNameList.append(location_name)
    #
    # def add_element_name(self, element_name):
    #     if element_name not in self._elementNameList:
    #         self._elementNameList.append(element_name)
    #
    # def add_sort(self, sort):
    #     if sort not in self._sortList:
    #         self._sortList.append(sort)

    def test_payload(self):
        return self._get_payload()
