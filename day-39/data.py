from pprint import pprint
import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/c1d1348bd34c463b9c606f2090785a89/copyOfFlightDeals/prices"


class DataManager:

    def __init__(self) -> None:
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update(self):
        for i in self.destination_data:
            end_point = f"{SHEETY_PRICES_ENDPOINT}/{i['id']}"
            pramter = {
                "price": {
                    "iataCode": i["iataCode"],
                }
            }

            response = requests.put(end_point, json=pramter)
            print(response.text)
