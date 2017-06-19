from cwb.data.data_set import DataSet
from cwb.data.locations import Location
from cwb.data.weather_element import WeatherElement

from cwb.api.open_data import OpenData
from cwb.data.source.time import Time


class OA0019(OpenData):
    def get_data_set(self):
        records = self._get_response().json()["records"]
        data_set = DataSet()

        for l in records["location"]:
            location = Location()
            location.location_name = l["locationName"]
            location.station_id = l["stationId"]

            for t in l["time"]:
                time = Time()
                time.obs_time = t["obsTime"]

                for we in t["weatherElement"]:
                    weather_element = WeatherElement()
                    weather_element.element_name = we["elementName"]
                    weather_element.element_value = we["elementValue"]
                    weather_element.element_measures = we["elementMeasures"]
                    time.weather_element_list.append(weather_element)

                location.time_list.append(time)

            data_set.location_list.append(location)

        return data_set

    def _set_payload(self, payload):
        pass

    def __init__(self, authorization):
        super(OA0019, self).__init__(authorization, "O-A0019-001")
