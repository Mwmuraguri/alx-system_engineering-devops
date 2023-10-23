#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys


def get_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(f"{base_url}users/{employee_id}")
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})

    if user_response.status_code != 200:
        sys.exit("User not found")

    if todos_response.status_code != 200:
        sys.exit("TODO list not found")

    user_data = user_response.json()
    todos_data = todos_response.json()

    completed_tasks = [task["title"] for task in todos_data if task["completed"]]

    return user_data, completed_tasks


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    user_data, completed_tasks = get_todo_list(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(user_data["todos"])))

    for task in completed_tasks:
        print("\t {}".format(task))

