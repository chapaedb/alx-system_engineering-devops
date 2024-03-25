#!/usr/bin/python3
"""
Script that retrieves information about a user's TODO list progress
from a REST API using their employee ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    employee_response = requests.get(todos_url)
    user_response = requests.get(user_url)

    todos_data = employee_response.json()
    user_name = user_response.json()['name']

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")
