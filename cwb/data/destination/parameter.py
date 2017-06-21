from cwb.data.destination.database import Parameter


class ParameterService:
    @staticmethod
    def set_parameter(session, source, time_id):
        parameter = Parameter()
        parameter.time_id = time_id
        if source.parameter_name is not None:
            parameter.name = source.parameter_name
        if source.parameter_value is not None:
            parameter.value = source.parameter_value
        if source.parameter_unit is not None:
            parameter.unit = source.parameter_unit
        session.add(parameter)

        return True
