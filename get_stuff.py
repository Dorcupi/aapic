import requests
import json

def get_stuff():
    response1 = requests.get("https://api.adviceslip.com/advice")

    response1 = response1.text

    response_info1 = json.loads(response1)

    quote = response_info1["slip"]["advice"]

    inspiration = "Temporarily offline"

    response3 = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})

    response3 = response3.json()

    dad_joke = response3["joke"]
    
    return [quote, inspiration, dad_joke]