import requests

url = "https://flight-radar1.p.rapidapi.com/aircrafts/list"

headers = {
	"X-RapidAPI-Key": "62907dd680msh3004a420941f57ap1abc43jsnf3b38a23d8d2",
	"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
with open("overlay.txt", "w") as ot:
	ot.write(data['rows'][0]["description"])