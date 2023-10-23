#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        sys.exit("Usage: {} <employee_id>".format(sys.argv[0]))

    employee_id = sys.argv[1]

    # Retrieve user and todos data
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    todos_response = requests.get(base_url + "todos", params={"userId": employee_id})

    if user_response.status_code != 200:
        sys.exit("User not found")

    if todos_response.status_code != 200:
        sys.exit("TODO list not found")

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos_data if task["completed"]]

    # Display the results
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(todos_data)))

    for task in completed_tasks:
        print("\t {}".format(task))

