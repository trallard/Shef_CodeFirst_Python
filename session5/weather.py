import requests
import json

id = "84600bca7507293656495e8972aec659"
payload = {'q':'Sheffield, UK', 'units':'metric', 'appid':id}

def query_weather(payload):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(endpoint, params=payload)
    return response

def jsonify(response):
    json_response = response.json()
    return json_response


response = query_weather(payload)
print(response.status_code)
print(response.text)

json_response = jsonify(response)
print("\n")
print(json_response)



with open("sample_weather.json", "w") as file:
    file.write(json.dumps(response.json(), indent=4))


# extracting the data you want
temperature = data['main']['temp']      # current temperature
temperature_unit = 'F' if (unit == 'imperial') else 'C'
conditions = data['weather'][0]['description'] #current weather
