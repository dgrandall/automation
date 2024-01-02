#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 21:40:20 2023

@author: d
"""

import requests
import json

#apiKey = input(str("Enter you Api Key Here: "))
apiKey = 'd7b402b3-8e1a-4dc1-83b9-d632c5c92b01'
print('----------------------------------------------------')
raw_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": apiKey,
        "n": 1,
        "min": 0,
        "max": 35,
        "replacement": True
    },
    'id':1
}

headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}

clean_data=json.dumps(raw_data)

response = requests.post(
    url='https://api.random.org/json-rpc/2/invoke',
    data=clean_data,
    headers=headers
    )

'''
old code 
print('METADATA CATEGORIES:')
print(response.headers) # this will show all the different metadata headers. 
print('----------------------------------------------------')
print(response.text)'''

my_dic = response.json()
#random_number = my_dic["result"]["random"]["data"][0] # pull the number out of the nested dictionary 
print(my_dic)


'''
#old code 
print(response.json())
print('----------------------------------------------------')
my_dic = (response.json())
result = my_dic["result"]
random = result["random"]
data = random["data"]
print(data[0])
print(type(data[0]))
print('----------------------------------------------------')'''


