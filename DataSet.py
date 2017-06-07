class DataSet:
    def __init__(self, data_set_info, contents, hazard_conditions, locations, location, time, weather_element,
                 parameter_set, parameter, resource, report, tsunami, earthquake):
        self.DataSetInfo = data_set_info
        self.Contents = contents
        self.HazardConditions = hazard_conditions
        self.Locations = locations
        self.Location = location
        self.Time = time
        self.WeatherElement = weather_element
        self.ParameterSet = parameter_set
        self.Parameter = parameter
        self.Resource = resource
        self.Report = report
        self.Tsunami = tsunami
        self.Earthquake = earthquake
