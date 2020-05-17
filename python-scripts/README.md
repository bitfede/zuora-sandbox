# Python scripts to query Zuora APIs

## Scripts:

### `query-product-catalog.py`

Usage:
```
usage: query-product-catalog.py [-h] -u User -p Password

Get the products in your Zuora catalog

optional arguments:
  -h, --help            show this help message and exit
  -u User, --user User  Your Zuora username
  -p Password, --password Password
                        Your Zuora password
```

Example:

```
$ ./query-product-catalog.py -u "user@example.com+testdrive" -p 'examplePassword'

[*] Fetching products...
[*] Here are the products:
> CloudStream SaaS Professional Edition 	 {id: f2b5989143f80278baa7c93604c6fa54}
> CloudStream Support Platinum 	 {id: f2b598916ecdce9735cce00c72e1db3d}
> CloudStream Digital Access 	 {id: f2b59891ae1494eee2dd6b6003beb6b1}
> CloudStream Professional Services 	 {id: f2b59891d4648b3a8eead0fab85c7399}

```

### `create-account-and-subscribe.py`

Usage:

```
usage: create-account-and-subscribe.py [-h] -u User -p Password -i Product id
                                       -d New Customer Data

Create a customer account and subscribe him to the selected subscription ID

optional arguments:
  -h, --help            show this help message and exit
  -u User, --user User  Your Zuora username
  -p Password, --password Password
                        Your Zuora password
  -i Product id, --product-id Product id
                        The product id of the subscription we want to
                        subscribe the user to
  -d New Customer Data, --customer-data New Customer Data
                        The information about the new customer to create
```


Example:
```
$ ./create-account-and-subscribe.py -u "user@example.com+testdrive" -p 'examplePassword' -d '{ "name":"ABC Unlimited",  "currency":"USD",  "billToContact":{    "firstName":"Leo", "lastName":"Liu"  },  "soldToContact":{      "firstName":"Leo",      "lastName":"Liu",      "state":"CA",   "country":"USA" },  "creditCard":{    "cardType":"Visa",    "cardNumber":"4111111111111111",    "expirationMonth":10,    "expirationYear":2020,    "securityCode":"111"  }, "subscription":{    "contractEffectiveDate": "2016-10-01",    "termType":"TERMED",    "autoRenew":false,    "initialTerm":12,    "renewalTerm":12,    "subscribeToRatePlans":[      {        "productRatePlanId": ""      }    ]  } }' -i f2b5989143f80278baa7c93604c6fa54

[*] Creating customer and activating subscription #f2b5989143f80278baa7c93604c6fa54...
[+] Account 2c92c0fb574ee46801574ef42dea04a0 created and subscribed to f2b5989143f80278baa7c93604c6fa54
```
