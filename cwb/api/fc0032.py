from cwb.data.source.data_set import DataSet
from cwb.data.source.data_set_info import DataSetInfo
from cwb.data.source.locations import Location
from cwb.data.source.parameter_set import Parameter
from cwb.data.source.weather_element import WeatherElement

from cwb.api.open_data import OpenData
from cwb.data.source.time import Time


class FC0032(OpenData):
    def get_data_set(self):
        records = self._get_response().json()["records"]

        data_set_info = DataSetInfo()
        data_set_info.data_set_description = records["datasetDescription"]

        data_set = DataSet()
        data_set.data_set_info = data_set_info

        for l in records["location"]:
            location = Location()
            location.location_name = l["locationName"]

            for we in l["weatherElement"]:
                weather_element = WeatherElement()
                weather_element.element_name = we["elementName"]

                for t in we["time"]:
                    time = Time()
                    time.start_time = t["startTime"]
                    time.end_time = t["endTime"]

                    parameter = Parameter()
                    if t["parameter"].get("parameterName", None) is not None:
                        parameter.parameter_name = t["parameter"]["parameterName"]
                    if t["parameter"].get("parameterValue", None) is not None:
                        parameter.parameter_value = t["parameter"]["parameterValue"]
                    if t["parameter"].get("parameterUnit", None) is not None:
                        parameter.parameter_unit = t["parameter"]["parameterUnit"]
                    time.Parameter = parameter

                    weather_element.time_list.append(time)

                location.weather_element_list.append(weather_element)

            data_set.location_list.append(location)

        return data_set

    def _set_payload(self, payload):
        pass

    def __init__(self, authorization, location_name_list=[]):
        super(FC0032, self).__init__(authorization, "F-C0032-001", location_name_list=location_name_list)
