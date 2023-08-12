import requests


def get_inspo_quote():
    category = 'inspirational'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    api_key = 'Zu3DasmIkTOY9/xNQFPEDg==zSkWG4DY0AS1S3Av'

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        quote_data = response.json()
        random_quote = quote_data[0]['quote']
        return random_quote
    else:
        return "Error fetching quote"