#!/usr/bin/python3
"""
Script that retrieves information about a user's TODO list progress
from a REST API using their employee ID
and exports the data in JSON format.
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
    username = user_response.json()['username']

    total_tasks = []
    update_user = {}

    for task in todos_data:
        total_tasks.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username,
            }
        )
    update_user[employee_id] = total_tasks

    file_json = employee_id + ".json"
    with open(file_json, 'w') as f:
        json.dump(update_user, f)
