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