#!/usr/bin/python3
"""
Fetches and saves an employee's TODO list progress in a JSON file.
"""
import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # Base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Construct API endpoints
    user_endpoint = f'{base_url}users?id={employee_id}'
    todos_endpoint = f'{base_url}todos?userId={employee_id}'

    # Fetch user information
    user_data = requests.get(user_endpoint).json()
    username = user_data[0].get('username')
    user_id = user_data[0].get('id')

    # Dictionary to hold the user's TODOs
    user_todos = {}
    with open(f'{user_id}.json', mode='w') as file:
        # Fetch user's TODOs
        todos_data = requests.get(todos_endpoint).json()

        # Extract relevant TODO details
        todo_list = [
            {'task': todo.get('title'),
             'completed': todo.get('completed'),
             'username': username}
            for todo in todos_data
        ]

        # Store TODOs in a dictionary and save to a JSON file
        user_todos[user_id] = todo_list
        json.dump(user_todos, file)
