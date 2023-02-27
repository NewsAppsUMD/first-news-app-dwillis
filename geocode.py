import requests

API_KEY = "106150bf9be0fc241d211ef8e7aa87c40eb66f9a"

base_url = f"https://api.geocodify.com/v2/geocode?api_key={API_KEY}&q="

r = requests.get(base_url + "1djlklkdjeljdlkedjledjledjl")

print(r.json()['response']['features'][0]['geometry']['coordinates'])