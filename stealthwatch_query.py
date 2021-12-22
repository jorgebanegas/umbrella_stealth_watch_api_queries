"""
Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests 
import pprint
import stealth_watch_helpers as sw
import csv
from apscheduler.schedulers.blocking import BlockingScheduler
import config
import datetime

def main():
    with requests.Session() as s:
    # all cookies received will be stored in the session object
        results = sw.authenticate(s)

        tenants = sw.get_tenants(s)["data"]
        print("Stealthwatch tenants : ")
        pprint.pprint(tenants)

        # choosing the first tenant from the list
        tenant = str(tenants[0]["id"])

        incidents = sw.get_incidents(s)

        try:
            data = incidents["data"]
            with open('sealth_watch_incidents.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = list(data[0].keys()))
                writer.writeheader()
                writer.writerows(data)

        except Exception as e: 
            print(e)
            print("error creating csv, no entries were queried")

        pprint.pprint(incidents)

sched = BlockingScheduler()
sched.add_job(main, trigger='interval', seconds=config.script_interval, next_run_time=datetime.datetime.now(), misfire_grace_time=10)  # main thread to query meraki
sched.start()