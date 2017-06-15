from cwb.api.Enum import Format
from cwb.api.OpenData import OpenData
from cwb.data.contents import Contents
from cwb.data.data_set import DataSet
from cwb.data.data_set_info import DataSetInfo
from cwb.data.locations import Locations, Location
from cwb.data.parameter_set import Parameter
from cwb.data.time import Time
from cwb.data.WeatherElement import WeatherElement


class FD0047(OpenData):
    def get_data_set(self):
        records = self.get_response().json()["records"]

        contents = Contents()
        contents.ContentDescription = records["contentDescription"]

        data_set = DataSet()
        data_set.Contents = contents

        for ls in records["locations"]:
            locations = Locations()

            data_set_info = DataSetInfo()
            data_set_info.DataSetDescription = ls["datasetDescription"]
            locations.DataSetInfo = data_set_info

            if ls.get("locationsName", None) is not None:
                locations.LocationsName = ls["locationsName"]
            locations.DataId = ls["dataid"]

            for l in ls["location"]:
                location = Location()
                location.LocationName = l["locationName"]
                if l.get("geocode", None) is not None:
                    location.GeoCode = l["geocode"]
                if l.get("lat", None) is not None:
                    location.Lat = l["lat"]
                if l.get("lon", None) is not None:
                    location.Lon = l["lon"]

                for we in l["weatherElement"]:
                    weather_element = WeatherElement()
                    weather_element.ElementName = we["elementName"]
                    if we.get("elementMeasure", None) is not None:
                        weather_element.ElementMeasure = we["elementMeasure"]

                    for t in we["time"]:
                        time = Time()
                        if t.get("startTime", None) is not None:
                            time.StartTime = t["startTime"]
                        if t.get("endTime", None) is not None:
                            time.EndTime = t["endTime"]
                        if t.get("dataTime", None) is not None:
                            time.DataTime = t["dataTime"]
                        if t.get("elementValue", None) is not None:
                            time.ElementValue = t["elementValue"]

                        if t.get("parameter", None) is not None:
                            parameter_list = []
                            for p in t["parameter"]:
                                parameter = Parameter()
                                if p.get("parameterName", None) is not None:
                                    parameter.ParameterName = p["parameterName"]
                                if p.get("parameterValue", None) is not None:
                                    parameter.ParameterValue = p["parameterValue"]
                                if p.get("parameterUnit", None) is not None:
                                    parameter.ParameterUnit = p["parameterUnit"]
                            time.Parameter = parameter_list

                        weather_element.TimeList.append(time)

                    location.WeatherElementList.append(weather_element)

                locations.LocationList.append(location)

            data_set.LocationsList.append(locations)

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

        if self._data_location_id == "093" and len(self._locationIdList) != 0:
            if payload is None:
                payload = {}
            payload["locationId"] = ",".join(li for li in self._locationIdList)

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

    def __init__(self, authorization, data_location_id):
        self._data_location_id = data_location_id
        self._data_id = "F-D0047-" + self._data_location_id
        super(FD0047, self).__init__(self._data_id, authorization)
        self._limit = -1
        self._offset = 0
        self._format = Format.json
        if self._data_location_id == "093":
            self._locationIdList = []
        self._locationName = self._data_id
        self._elementNameList = []
        self._sortList = []

    def set_limit(self, limit):
        self._limit = limit

    def set_offset(self, offset):
        self._offset = offset

    def set_format(self, format_enum):
        self._format = format_enum

    def add_location_id(self, location_id):
        if self._data_location_id == "093":
            self._locationIdList.append(location_id)

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
