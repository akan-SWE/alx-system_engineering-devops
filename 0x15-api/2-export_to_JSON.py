#!/usr/bin/python3
"""returns information about a given employee's TODO list progress
and saves this info in a json file
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # Setup urls and query strings
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users?id={employee_id}'
    todos = f'todos?userId={employee_id}'
    done = f'{todos}&completed=true'

    # Get information about the employee such as their username and id
    user_data = requests.get(f"{url}{users}").json()
    username = user_data[0].get('username')
    user_id = user_data[0].get('id')

    user_todos_data = {}
    with open(f'{user_id}.json', mode='w') as file:
        # Get todos for the employee
        todos_data = requests.get(f'{url}{todos}').json()

        # Extract title, username and task completed status of the todos
        extracted_todo = [
            {'task': task.get('title'),
            'completed': task.get('completed'), 'username': username}
            for task in todos_data
        ]

        # Store extracted todo in a dictionary and save to a JSON file
        user_todos_data[user_id] = extracted_todo
        json.dump(user_todos_data, file)
