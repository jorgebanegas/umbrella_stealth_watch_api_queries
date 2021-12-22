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
import json
import pprint
import config

def authenticate(api_key):

    url = "https://management.api.umbrella.com/auth/v2/oauth2/token"

    payload={}
    headers = {
    'Authorization': 'Basic ' + api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()

    return response['access_token']

def total_proxy_requests(start,end,access_token):
    url = "https://reports.api.umbrella.com/v2/organizations/" + config.umbrella_org_id + "/total-requests/proxy?from=" + str(int(start)) + "&" + "to=" + str(int(end))

    payload={}
    headers = {
    'Authorization': 'Bearer ' + access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def total_dns_requests(start,end,access_token):
    url = "https://reports.api.umbrella.com/v2/organizations/" + config.umbrella_org_id + "/total-requests/dns?from=" + str(int(start)) + "&" + "to=" + str(int(end))

    payload={}
    headers = {
    'Authorization': 'Bearer ' + access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def blocked_proxy_activity(start,end,access_token):
    url = "https://reports.api.umbrella.com/v2/organizations/" + config.umbrella_org_id + "/activity/proxy?verdict=blocked&from=" + str(int(start)) + "&" + "to=" + str(int(end)) + "&limit=" + str(config.api_results_limit)

    payload={}
    headers = {
    'Authorization': 'Bearer ' + access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def blocked_dns_activity(start,end,access_token):
    url = "https://reports.api.umbrella.com/v2/organizations/" + config.umbrella_org_id + "/activity/proxy?verdict=blocked&from=" + str(int(start)) + "&" + "to=" + str(int(end)) + "&limit=" + str(config.api_results_limit)

    payload={}
    headers = {
    'Authorization': 'Bearer ' + access_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()