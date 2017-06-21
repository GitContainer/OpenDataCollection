from cwb.data.source.data_set import DataSet
from cwb.data.source.data_set_info import DataSetInfo
from cwb.data.source.locations import Locations, Location
from cwb.data.source.parameter_set import Parameter
from cwb.data.source.time import Time
from cwb.data.source.weather_element import WeatherElement

from cwb.api.open_data import OpenData
from cwb.data.source.contents import Contents


class FD0047(OpenData):
    def get_data_set(self):
        records = self._get_response().json()["records"]

        contents = Contents()
        contents.content_description = records["contentDescription"]

        data_set = DataSet()
        data_set.contents = contents

        for ls in records["locations"]:
            locations = Locations()

            data_set_info = DataSetInfo()
            data_set_info.data_set_description = ls["datasetDescription"]
            locations.data_set_info = data_set_info

            if ls.get("locationsName", None) is not None:
                locations.LocationsName = ls["locationsName"]
            locations.DataId = ls["dataid"]

            for l in ls["location"]:
                location = Location()
                location.location_name = l["locationName"]
                if l.get("geocode", None) is not None:
                    location.geo_code = l["geocode"]
                if l.get("lat", None) is not None:
                    location.lat = l["lat"]
                if l.get("lon", None) is not None:
                    location.lon = l["lon"]

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
                                parameter_list.append(parameter)

                            time.Parameter = parameter_list

                        weather_element.time_list.append(time)

                    location.weather_element_list.append(weather_element)

                locations.location_list.append(location)

            data_set.locations_list.append(locations)

        return data_set

    def add_location_id(self, location_id):
        if self.__data_location_id == "093":
            self.__location_id_list.append(location_id)

    def _set_payload(self, payload):
        if self.__data_location_id == "093" and len(self.__location_id_list) != 0:
            if payload is None:
                payload = {}
            payload["locationId"] = ",".join(li for li in self.__location_id_list)

    def __init__(self, authorization, data_location_id, location_name=None, location_name_list=[]):
        self.__data_location_id = data_location_id
        self._data_id = "F-D0047-" + self.__data_location_id
        super(FD0047, self).__init__(authorization, self._data_id, location_name=location_name,
                                     location_name_list=location_name_list)

        if self.__data_location_id == "093":
            self.__location_id_list = []
