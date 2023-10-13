import requests
from datetime import datetime
end_point = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
app_id = "5d04f10f"

app_key = "91c868cfd4494ef4199b0427264d657f"


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
pramter = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}
headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
}

response = requests.post(url=exercise_endpoint, json=pramter, headers=headers)
exercise = response.json()["exercises"][0]


url_ = 'https://api.sheety.co/c1d1348bd34c463b9c606f2090785a89/workouts/workouts'


pramter1 = {
    "workouts": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise['name'],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
    }

}
sheet_response = requests.post(url_, json=pramter1)
print(sheet_response.text)
