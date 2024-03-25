#!/usr/bin/python3
"""
Script that retrieves information about a user's TODO list progress
from a REST API using their employee ID
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    session = requests.Session()

    employee_id = argv[1]
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    employee_response = session.get(todos_url)
    user_response = session.get(user_url)

    todos_data = employee_response.json()
    user_name = user_response.json()['name']

    total_tasks = 0

    for task in todos_data:
        if task['completed']:
            total_tasks += 1

    print("Employee {} has completed tasks: {}/{}".format(user_name, total_tasks, len(todos_data)))

    for task in todos_data:
        if task['completed']:
            print("\t" + task.get('title'))
