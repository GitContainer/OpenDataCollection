import json
import requests
import unittest


# https://www.dataquest.io/blog/python-api-tutorial/
class TestRequests(unittest.TestCase):
    def test200(self):
        response = requests.get("http://api.open-notify.org/iss-now.json")
        self.assertEqual(200, response.status_code)

    def test404(self):
        response = requests.get("http://api.open-notify.org/iss-pass")
        self.assertEqual(404, response.status_code)

    def test400(self):
        response = requests.get("http://api.open-notify.org/iss-pass.json")
        self.assertEqual(400, response.status_code)

    def testQueryParameters(self):
        parameters = {"lat": 40.71, "lon": -74}
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        # self.assertNotEqual(None, response.content)
        # print(response.content)
        data = response.json()
        print(type(data))
        print(data["message"])

    def testJSON(self):
        best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
        print(type(best_food_chains))

        best_food_chains_string = json.dumps(best_food_chains)
        print(type(best_food_chains_string))
        print(type(json.loads(best_food_chains_string)))

        fast_food_franchise = {
            "Subway": 24722,
            "McDonalds": 14098,
            "Starbucks": 10821,
            "Pizza Hut": 7600
        }
        fast_food_franchise_string = json.dumps(fast_food_franchise)
        print(type(fast_food_franchise_string))
