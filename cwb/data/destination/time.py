from cwb.data.destination.database import Time
from cwb.data.destination.parameter import ParameterService


class TimeService:
    @staticmethod
    def set_time(session, source, task_id, location_id, weather_element_id):
        time = Time()
        time.task_id = task_id
        time.location_id = location_id
        time.weather_element_id = weather_element_id
        if source.start_time is not None:
            time.start_time = source.start_time
        if source.end_time is not None:
            time.end_time = source.end_time
        if source.data_time is not None:
            time.data_time = source.data_time
        if source.element_value is not None:
            time.element_value = source.element_value
        session.add(time)
        session.flush()

        if source.parameter is not None:
            for p in source.parameter:
                if not ParameterService.set_parameter(session, p, time.time_id):
                    return False

        return True
