import requests
import json

def get_stuff():
    response1 = requests.get("https://api.adviceslip.com/advice")

    response1 = response1.text

    response_info1 = json.loads(response1)

    quote = response_info1["slip"]["advice"]

    response2 = requests.get("https://api.goprogram.co.uk/inspiration")

    response2 = response2.text

    response_info2 = json.loads(response2)

    inspiration = response_info2["quote"]

    response3 = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})

    response3 = response3.json()

    dad_joke = response3["joke"]
    
    return [quote, inspiration, dad_joke]