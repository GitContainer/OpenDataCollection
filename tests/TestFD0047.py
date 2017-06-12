import unittest

from cwb.api.Enum import Format, Sort
from cwb.api.FD0047 import FD0047, ElementName


class TestFD0047(unittest.TestCase):
    def test_payload_none(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        payload = api.test_payload()
        self.assertEqual(None, payload)

    def test_payload(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        api.set_limit(2)
        api.set_offset(1)
        api.set_format(Format.xml)
        api.set_location_name("頭城鎮")
        api.add_element_name(ElementName.Wx)
        api.add_element_name(ElementName.Wind)
        api.add_sort(Sort.time)

        payload = api.test_payload()
        print(payload)

    # def test_get_response_no_payload(self):
    #     api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
    #     response = api.get_response()
    #     data = response.json()
    #     print(data)

    def test_get_response_payload(self):
        api = FD0047("CWB-C9C20F8C-2237-46EB-B015-C52E09A8BDDB", "001")
        api.set_limit(2)
        api.set_offset(1)
        # api.set_format(Format.xml)
        api.set_location_name("頭城鎮")
        api.add_element_name(ElementName.Wx)
        api.add_element_name(ElementName.Wind)
        api.add_sort(Sort.time)

        response = api.get_response()
        data = response.json()
        print(data)
