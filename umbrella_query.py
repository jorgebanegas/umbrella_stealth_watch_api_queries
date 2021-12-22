import requests
import json
import pprint
import config
import umbrella_helpers as u
import time
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

import csv
import logging.handlers
import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

def main():

    # retrieve API token using API key that was generated from the umbrella dashboard

    access_token = u.authenticate(config.umbrella_api_key)

    today = int(time.time())*1000

    week_ago = today - 604800000
    hour_ago = today - 3600000

    #total_proxy_requests = u.total_proxy_requests(start=week_ago,end=today,access_token=access_token)

    #proxy_activity = u.blocked_proxy_activity(start=week_ago,end=today,access_token=access_token)

    total_dns_requests = u.total_dns_requests(start=week_ago,end=today,access_token=access_token)

    dns_activity = u.blocked_dns_activity(start=week_ago,end=today,access_token=access_token)

    try:
        with open('umbrella_blocked_dns_requests.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = list(dns_activity["data"][0].keys()))
            writer.writeheader()
            writer.writerows(dns_activity["data"])

        print("total dns requests")
        pprint.pprint(total_dns_requests["data"])
    except:
        print("error creating csv, no entries were queried")

sched = BlockingScheduler()
sched.add_job(main, trigger='interval', seconds=config.script_interval, next_run_time=datetime.datetime.now(), misfire_grace_time=10)  # main thread to query meraki
sched.start()

