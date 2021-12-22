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
import json
import config

def authenticate(s):
    payload= 'username=' + config.swc_username + '&password=' +config.swc_password

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    results = s.post("https://" + config.swc_ip_address + "/token/v2/authenticate",headers=headers,data=payload,verify=False)

    return results.json()

def get_tenants(s):

    headers = {}

    results = s.get("https://" + config.swc_ip_address + "/sw-reporting/v1/tenants",headers=headers,verify=False)

    return results.json()

def get_incidents(s):

    headers = {}

    results = s.get("https://" + config.swc_ip_address + "/sw-reporting/v2/tenants/0/incidents?limit=" + str(config.api_results_limit),headers=headers,verify=False)

    return results.json()