import requests
END_POINT = "https://docs.google.com/spreadsheets/d/1AJRA6ULssl0Qe7-SqoZwVMbSY2X9DSEa1vyQRUPvRyE/edit#gid=0"


class Users:

    def __init__(self) -> None:
        self.users = []
        self.all_user()
        print(self.users)

    def all_user(self):
        response = requests.get(END_POINT)
        self.users.append(response.json())

    def check_user(self, name, lname, email):
        for i in self.users:
            print(i)
            if email == i[0]['email']:
                return False
            else:
                self.create_user(name=name, lname=lname, email=email)
                return True

    def create_user(self, name, lname, email):
        pramter = {
            "sheet1": {
                "name": name,
                "lastName": lname,
                "email": email,
            }
        }
        response = requests.post(END_POINT, json=pramter)
        print(response.text)
