import requests

def get_APOD(date):
    """This will do the request on the NASA api"""
    payload = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key' : 'DEMO_KEY',
              'date' : date}

    response = requests.get(payload, params = params)
    return response.json()