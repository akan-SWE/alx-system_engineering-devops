#!/usr/bin/python3
"""returns information about a given employee's TODO list progress"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    users = f'users?id={employee_id}'
    todos = f'todos?userId={employee_id}'
    done = f'{todos}&completed=true'

    user_data = requests.get(f"{url}{users}").json()
    name = user_data[0].get('name')
    todos_data = requests.get(f'{url}{todos}').json()
    todos_done = requests.get(f'{url}{done}').json()

    doneN = len(todos_done)
    totalN = len(todos_data)

    print(f'Employee {name} is done with tasks({doneN}/{totalN}):')
    for task in todos_done:
        print(f"\t {task.get('title')}")
