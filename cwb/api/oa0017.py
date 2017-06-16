from cwb.api.open_data import OpenData


class OA0017(OpenData):
    def get_data_set(self):
        pass

    def _set_payload(self, payload):
        pass

    def __init__(self, authorization):
        super(OA0017, self).__init__("O-A0017-001", authorization)
