from requests import *

question = get(
    url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")


question_data = question.json()["results"]
