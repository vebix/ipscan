#!/usr/bin/env python
import requests
import sys
import os
import argparse
from colorama import Fore as F, init
w = F.WHITE
r = F.RED
init()
parser = argparse.ArgumentParser()
parser.add_argument("ip", help='the target ip')
args = parser.parse_args()
url = f"http://ip-api.com/json/{args.ip}"
try:
    req = requests.get(url)
except Exception as e:
    print(f"\n{r}IP not found or no network at the moment.{w}")
    sys.exit(1)
inf = req.json()
print(f'{r}IPSCAN{w} 1.2')
print(f'\nIP: {r}{inf["query"]}')
print(f'{w}ASN: {r}{inf["as"]}')
print(f'{w}City: {r}{inf["city"]}')
print(f'{w}Country: {r}{inf["country"]}')
print(f'{w}Country code: {r}{inf["countryCode"]}')
print(f'{w}ISP: {r}{inf["isp"]}')
print(f'{w}Latitude: {r}{inf["lat"]}')
print(f'{w}Longtitude: {r}{inf["lon"]}')
print(f'{w}Organisation: {r}{inf["org"]}')
print(f'{w}Region code: {r}{inf["region"]}')
print(f'{w}Region name: {r}{inf["regionName"]}')
print(f'{w}Timezone: {r}{inf["timezone"]}')
print(f'{w}Zip: {r}{inf["zip"]}{w}')
print(f'\nPowered by {r}@vebix{w}')