#!/usr/bin/python3
"""
Script that retrieves information about a user's TODO list progress
from a REST API using their employee ID
and exports the data in CSV format.
"""

import csv
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

    total_tasks = 0

    for task in todos_data:
        if task['completed']:
            total_tasks += 1

    file_csv = employee_id + '.csv'

    with open(file_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])
