from cwb.data.destination.database import Location


class LocationService:
    @staticmethod
    def set_location(session, source):
        location = Location()
        location.name = source.location_name
        if source.geo_code is not None:
            location.geo_code = source.geo_code
        if source.lat is not None:
            location.lat = source.lat

