import unittest


class TestSomething(unittest.TestCase):
    def test_encode(self):
        string = u"多雲。 降雨機率 0%。 溫度攝氏30度。 悶熱。 偏東風 平均風速小於1級(每秒<=1公尺)。 相對濕度為74%。"
        print(len(string))
