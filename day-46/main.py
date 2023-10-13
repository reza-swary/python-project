import requests
from bs4 import BeautifulSoup

songs_list = ""
music_list = []
api = "https://www.billboard.com/charts/hot-100/2008-01-05/"
response = requests.get(api)
soup = BeautifulSoup(response.text, "html.parser")
song_name = soup.find_all(name="h3", class_="c-title")
for songs in song_name:
    music = songs.getText()
    songs_list += music
# for i in songs_list.split("\n"):
#     if i == "" or i == "\t" or i == "\t\t":
#         pass
#     else:
#         music_list.append(i)

print(songs_list.strip())
