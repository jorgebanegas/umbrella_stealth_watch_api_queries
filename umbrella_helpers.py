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