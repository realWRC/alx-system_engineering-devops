#!/usr/bin/python3
"""Save employee data into a json file"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    r = requests.get(url)
    users = r.json()

    dictionary = {}
    for user in users:
        id = user.get('id')
        username = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
        r = requests.get(url + "/todos/")
        jobs = r.json()
        dictionary[id] = []
        for job in jobs:
            dictionary[id].append({
                "task": job.get('title'),
                "completed": job.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
