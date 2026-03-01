
import requests

location = input("please enter the place that you want to search: ")

def weather(location):
    url = "https://wttr.in/" + location + "?format=4"
    r = requests.get(url)
    return r.text.strip()

print(weather(location))
