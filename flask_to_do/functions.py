import requests


def get_inspirational_quote():
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


# checks that there are no more than 15 tasks in each to-do list
def todo_length(todo_list):
    return len(todo_list) <= 10


# checks that task is not empty and no longer than 40 characters
def task_length(task):
    return 0 < len(task) <= 40

