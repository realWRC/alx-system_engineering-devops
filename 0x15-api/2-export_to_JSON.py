#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and saves it to json file.
"""

import requests
import json
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    r = requests.get(url)
    username = r.json().get('username')

    r = requests.get(url + "/todos")
    jobs = r.json()

    data = {id: []}
    for job in jobs:
        data[id].append({
            "task": job.get("title"),
            "completed": job.get("completed"),
            "username": username
        })

    with open('{}.json'.format(id), 'w') as f:
        json.dump(data, f)
