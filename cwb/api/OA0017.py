from cwb.api.OpenData import OpenData


class OA0017(OpenData):
    def _get_payload(self):
        pass

    def get_data_set(self):
        pass

    def __init__(self, authorization):
        super(OA0017, self).__init__("O-A0017-001", authorization)
