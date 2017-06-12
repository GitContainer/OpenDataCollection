import unittest

from cwb.api.Enum import Format, Sort
from cwb.api.FC0032 import FC0032, ElementName


class TestFC0032(unittest.TestCase):
    def test_payload_none(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        payload = api.test_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        api.set_limit(2)
        api.set_offset(1)
        api.set_format(Format.xml)
        api.add_location_name("宜蘭縣")
        api.add_location_name("花蓮縣")
        api.add_element_name(ElementName.Wx)
        api.add_element_name(ElementName.PoP)
        api.add_sort(Sort.time)

        payload = api.test_payload()
        print(payload)

    def test_get_response_no_payload(self):
        api = FC0032("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB")
        response = api.get_response()
        data = response.json()
        print(data)
