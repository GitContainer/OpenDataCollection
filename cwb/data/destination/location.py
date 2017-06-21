from cwb.data.destination.database import Location
from cwb.data.destination.weather_element import WeatherElementService


class LocationService:
    @staticmethod
    def set_location(session, source, task_id):
        row = session.query(Location).filter_by(name=source.location_name).first()
        if row:
            location_id = row.location_id
        else:
            location = Location()
            location.name = source.location_name
            if source.geo_code is not None:
                location.geo_code = source.geo_code
            if source.lat is not None:
                location.lat = source.lat
            if source.lon is not None:
                location.lon = source.lon
            session.add(location)
            session.flush()
            location_id = location.location_id

        for we in source.weather_element_list:
            if not WeatherElementService.set_weather_element(session, we, task_id, location_id):
                return False

        return True
