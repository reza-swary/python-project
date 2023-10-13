import requests

end_point = "https://api.openweathermap.org/data/2.5/forecast"
Api_key = "9bae887dffb5f66fe5907ae465310981"

weather_params = {
    "lat": 31.273542,
    "lon": 48.645327,
    "appid": Api_key,
}

response = requests.get(end_point, params=weather_params)

data = []
for i in range(0, 13):
    weather_data = response.json()["list"][i]["weather"][0]
    data.append(weather_data)
    print(weather_data["id"])
    if weather_data["id"] < 700:
        print("bring ombrla")
