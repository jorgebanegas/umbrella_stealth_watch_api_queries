import requests
import json
import pprint
import config
import umbrella_helpers as u
import time
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

