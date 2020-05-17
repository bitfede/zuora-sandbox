#!/usr/bin/env python3

import argparse
import requests
import json

# get user-provided keyword and store it into a variable
parser = argparse.ArgumentParser(description='Create a customer account and subscribe him to the selected subscription ID')
parser.add_argument('-u', '--user', required=True, metavar='User', help='Your Zuora username')
parser.add_argument('-p', '--password', required=True, metavar='Password', help='Your Zuora password')
parser.add_argument('-i', '--product-id', required=True, metavar='Product id', help="The product id of the subscription we want to subscribe the user to")
parser.add_argument('-d', '--customer-data', required=True, metavar='New Customer Data', help="The information about the new customer to create")

args = vars(parser.parse_args())
apiAccessKeyId = args['user']
apiSecretAccessKey = args['password']
product_id = args['product_id']
customer_data = json.loads(args['customer_data'])

print(f"[*] Creating customer and activating subscription #{product_id}...")

# assign product id to the customer data dictionary
customer_data['subscription']['subscribeToRatePlans'][0]['productRatePlanId'] = product_id

# shoot an API call to the backend service
base_url = 'https://rest.apisandbox.zuora.com/v1'
api_method = '/accounts'
headers = {
    'apiAccessKeyId': apiAccessKeyId,
    'apiSecretAccessKey': apiSecretAccessKey
}

full_url = f"{base_url}{api_method}"

response = requests.post(full_url, headers=headers, data=customer_data)

res_json = response.json()

print(res_json)
