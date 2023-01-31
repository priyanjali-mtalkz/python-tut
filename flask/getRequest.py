import requests
URL ="http://maps.googleapis.com/maps/api/geocode/json"
location = "Delhi Technological University"

PARAMS = {'address':location}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['long']
formatted_address = data['results'][0]['formatted_address']

print("Latitude: %s\n Formatted Address: %s" %(latitude,longitude,formatted_address))