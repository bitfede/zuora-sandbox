#!/usr/bin/env python3

import argparse
import requests
import json

# get user-provided keyword and store it into a variable
parser = argparse.ArgumentParser(description='Get the products in your Zuora catalog')
parser.add_argument('-u', '--user', required=True, metavar='User', help='Your Zuora username')
parser.add_argument('-p', '--password', required=True, metavar='Password', help='Your Zuora password')

args = vars(parser.parse_args())
apiAccessKeyId = args['user']
apiSecretAccessKey = args['password']

print("[*] Fetching products...")

# shoot an API call to the backend service
base_url = 'https://rest.apisandbox.zuora.com/v1'
api_method = '/catalog/products'
headers = {
    'apiAccessKeyId': apiAccessKeyId,
    'apiSecretAccessKey': apiSecretAccessKey
}

full_url = f"{base_url}{api_method}"

response = requests.get(full_url, headers=headers)

res_json = response.json()

print("[*] Here are the products:")

for product in res_json['products']:
    print(">", product['name'], "\t", "{id:", f"{product['id']}" + "}")
