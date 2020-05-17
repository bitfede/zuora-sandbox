# Python scripts to query Zuora APIs

## Scripts:

### `create-account-and-subscribe.py`

Manual:
```
usage: query-product-catalog.py [-h] -u User -p Password

Get the products in your Zuora catalog

optional arguments:
  -h, --help            show this help message and exit
  -u User, --user User  Your Zuora username
  -p Password, --password Password
                        Your Zuora password
```

Example usage:

```
$ ./query-product-catalog.py -u "user@example.com+testdrive" -p 'examplePassword'

[*] Fetching products...
[*] Here are the products:
> CloudStream SaaS Professional Edition 	 {id: f2b5989143f80278baa7c93604c6fa54}
> CloudStream Support Platinum 	 {id: f2b598916ecdce9735cce00c72e1db3d}
> CloudStream Digital Access 	 {id: f2b59891ae1494eee2dd6b6003beb6b1}
> CloudStream Professional Services 	 {id: f2b59891d4648b3a8eead0fab85c7399}
> CloudStream Training Basic 	 {id: f2b59891c28b29f88bdc337d9a9feac3}
> CloudStream Storage Starter 	 {id: f2b59891faea49f7742a0e237c7c1eac}
> CloudStream Promotions 	 {id: f2b5989124529a6e4b5fd8b39588426a}
> CloudStream PaaS General Purpose 	 {id: f2b59891d4029527616c593932949b96}
> CloudStream Top Down Bundle 	 {id: f2b59891daab9f46868ec1bf87933f07}
> CloudStream Software Design 	 {id: f2b59891ce553ace4a839a8629549409}

```
