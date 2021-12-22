# umbrella_stealth_watch_api_queries
prototype code that queries information from Cisco Umbrella and Stealthwatch and then converts the data into a csv file

## Contacts
* Jorge Banegas

## Solution Components
* Cisco Umbrella
* Cisco Stealthwatch

## Installation/Configuration

(optional) This first step is optional if user wants to leverage a virtual environment to install python packages

```shell
pip install virtualenv
virtualenv env
source env/bin/activate
```

Install python dependencies 

```shell
pip install -r requirements.txt
```

Include configuration details inside the config.py file.

Visit this link to generate an API key for Umbrella
(https://developer.cisco.com/docs/cloud-security/#!reporting-v2-introduction-authentication/generate-an-api-key)


Visit this link to find your organization ID for Umbrella
(https://docs.umbrella.com/deployment-umbrella/docs/find-your-organization-id)


```
umbrella_api_key = ''

api_results_limit = '1000'

# https://docs.umbrella.com/deployment-umbrella/docs/find-your-organization-id
umbrella_org_id = ''

# interval for script to run in seconds (launch function every 60 seconds)
script_interval = 60

swc_ip_address = ''
swc_username = ''
swc_password = ''
```

For the stealthwatch script to query results, you must activate CTA and the APIs for it. 

![/images/incidents_api_call.png](/images/incidents_api_call.png)


Response schema for Stealthwatch Incidents API call 

![/images/stealthwatch_response_schema.png](/images/stealthwatch_response_schema.png)


Response schema for Umbrealla DNS Activity API call 

![/images/stealthwatch_response_schema.png](/images/umbrella_response_schema.png)


## Usage

To launch the umbrella script (this script collects DNS blocked activity):


    (env) $ python umbrella_query.py 
   

To launch the stealthwatch script (this script collects DNS blocked activity CTA incidents):


    (env) $ python stealthwatch_query.py
    
If the script is unable to create a CSV file, that means the API call was not able to query any results.

If everything works out, you should see the creation of the CSV files once the script executes

sealth_watch_incidents.csv
umbrella_blocked_dns_requests.csv

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.

