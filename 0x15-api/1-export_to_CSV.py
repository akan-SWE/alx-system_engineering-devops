#!/usr/bin/python3
"""returns information about a given employee's TODO list progress
and save to a CSV file.
"""
import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    # Setup urls and query strings
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users?id={employee_id}'
    todos = f'todos?userId={employee_id}'
    done = f'{todos}&completed=true'

    # Get information about user
    user_info = requests.get(f"{url}{users}").json()
    user_name = user_info[0].get('username')
    user_id = user_info[0].get('id')

    # Create a csv file with name equals <userId>.csv
    with open(f'{user_id}.csv', mode='w') as file:
        # Get todos information and create a writer object
        todos_data = requests.get(f'{url}{todos}').json()
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

        # Insert each item in the todos data set as a row in the csv file
        for todo in todos_data:
            user_id = todo.get('userId')
            task_status = todo.get('completed')
            task_title = todo.get('title')
            writer.writerow([user_id, user_name, task_status, task_title])
