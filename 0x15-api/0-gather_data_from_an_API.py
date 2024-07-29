#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
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
    finished_list = []
    finished = 0

    for job in jobs:
        if job.get('completed'):
            finished_list.append(job)
            finished += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, finished, len(jobs)))

    for job in finished_list:
        print("\t {}".format(job.get("title")))
