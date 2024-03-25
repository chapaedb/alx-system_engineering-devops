#!/usr/bin/python3
"""
Script that retrieves information about each employee's TODO list progress
from a REST API and exports the data in JSON format.
"""

import json
import requests


if __name__ == "__main__":
    import json
    import requests

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todo_all = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                task_list.append(task_dict)
        todo_all[user.get('id')] = task_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all, f)
