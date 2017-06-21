from cwb.data.destination.database import WeatherElement
from cwb.data.destination.time import TimeService


class WeatherElementService:
    @staticmethod
    def set_weather_element(session, source, task_id, location_id):
        row = session.query(WeatherElement).filter_by(name=source.element_name).first()
        if row:
            weather_element_id = row.weather_element_id
        else:
            weather_element = WeatherElement()
            weather_element.name = source.element_name
            if hasattr(weather_element, "element_measure") and source.element_measure is not None:
                weather_element.measure = source.element_measure
            session.add(weather_element)
            session.flush()
            weather_element_id = weather_element.weather_element_id

        for t in source.time_list:
            if not TimeService.set_time(session, t, task_id, location_id, weather_element_id):
                return False

        return True
