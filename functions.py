import requests
from config import API_KEY  # Use the correct name in uppercase

def get_inspirational_quote():
    try:
        category = 'inspirational'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

        response = requests.get(api_url, headers={'X-Api-Key': API_KEY})  # Use the imported API_KEY

        if response.status_code == requests.codes.ok:
            quote_data = response.json()
            random_quote = quote_data[0]['quote']
            return random_quote
        else:
            return "Error fetching quote"
    except Exception as e:
        return "An error occurred while fetching a quote: " + str(e)


# checks that there are no more than 15 tasks in each to-do list
def todo_length(todo_list):
    return len(todo_list) <= 9


# checks that task is not empty and no longer than 40 characters
def task_length(task):
    return 0 < len(task) <= 40