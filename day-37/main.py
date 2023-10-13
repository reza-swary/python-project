import requests
import datetime
pixela = "https://pixe.la/v1/users/hamzh16/graphs/project1"
today = datetime.datetime.now()
user_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6"
}
token = {
    "X-USER-TOKEN": "swary2079"
}

response = requests.post(pixela, json=user_params, headers=token)


print(response.text)
