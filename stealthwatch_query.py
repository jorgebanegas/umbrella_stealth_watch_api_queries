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