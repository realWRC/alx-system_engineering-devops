#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress and saves it to csv file.
"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    r = requests.get(url)
    employee_name = r.json().get('name')

    r = requests.get(url + "/todos")
    jobs = r.json()

    with open("{}.csv".format(id), 'w') as f:
        for job in jobs:
            f.write('"{}","{}","{}","{}"\n'
                    .format(id, employee_name, job.get('completed'),
                            job.get('title')))
