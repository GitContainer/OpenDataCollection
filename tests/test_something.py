import os
import unittest


class TestSomething(unittest.TestCase):
    def test_encode(self):
        if os.path.isfile("..\setup.conf"):
            file = open("..\setup.conf", "r")

            line = file.readline()
            while line:
                print(line)
                line = file.readline()

            file.close()
