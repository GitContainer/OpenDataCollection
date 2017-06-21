from cwb.data.source.data_set import DataSet
from cwb.data.source.data_set_info import DataSetInfo
from cwb.data.source.locations import Location
from cwb.data.source.parameter_set import Parameter
from cwb.data.source.valid_time import ValidTime
from cwb.data.source.weather_element import WeatherElement

from cwb.api.open_data import OpenData
from cwb.data.source.time import Time


class FA0021(OpenData):
    def get_data_set(self):
        records = self._get_response().json()["records"]

        data_set_info = DataSetInfo()
        data_set_info.data_id = records["dataid"]
        data_set_info.note = records["note"]

        data_set = DataSet()
        data_set.data_set_info = data_set_info

        for l in records["location"]:
            location = Location()
            location.location_name = l["locationName"]
            location.station_id = l["stationId"]

            location.valid_time_list = []
            for vt in l["validTime"]:
                valid_time = ValidTime()
                valid_time.start_time = vt["startTime"]
                valid_time.end_time = vt["endTime"]

                valid_time.weather_element_list = []
                for we in vt["weatherElement"]:
                    weather_element = WeatherElement()
                    weather_element.element_name = we["elementName"]
                    if we.get("elementValue", None) is not None:
                        weather_element.element_value = we["elementValue"]

                    if we.get("time", None) is not None:
                        for t in we["time"]:
                            time = Time()
                            time.data_time = t["dataTime"]

                            parameter_list = []
                            for p in t["parameter"]:
                                parameter = Parameter()
                                parameter.parameter_name = p["parameterName"]
                                if p.get("parameterValue", None) is not None:
                                    parameter.parameter_value = p["parameterValue"]
                                if p.get("parameterMeasure", None) is not None:
                                    parameter.parameter_measure = p["parameterMeasure"]
                                parameter_list.append(parameter)
                            time.parameter = parameter_list
                            weather_element.time_list.append(time)

                    valid_time.weather_element_list.append(weather_element)

                location.valid_time_list.append(valid_time)

            data_set.location_list.append(location)

        return data_set

    def _set_payload(self, payload):
        pass

    def __init__(self, authorization, location_name_list=[]):
        super(FA0021, self).__init__(authorization, "F-A0021-001", location_name_list=location_name_list)
