#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 00:42:42 2022

@author: dan
"""
import requests
import json

CHARS ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # all of the possible characters, 36 in total from [0:35] 

apiKey = input(str("Enter you Api Key Here: "))


# put the new ran generator program here 
def genRanNumberList(apiKey): 
    raw_data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": apiKey,
            "n": 100, # the number of numbers 
            "min": 1, # lowest value 
            "max": 35, # highest value 
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
    
    my_dic = (response.json()) # store this json output as a variable (it is already in dictionary format )
    random_numbers = my_dic["result"]["random"]["data"] # pull the numbers out of the nested dictionary 
    return (random_numbers)




otpadkey = [] 
for i in range(1,101): # generate 100 keys (independed of the numbers generated)
    for ran_num in genRanNumberList(apiKey): # iterate throught the list of 100 random numbers 
        otpadkey.append(CHARS[ran_num])
    otpadkey=''.join(otpadkey)     # for use in lists 
    otpkeysfile = open('/home/d/Documents/Cryptography/otpkeysfile.txt','a') # input your own file path. Ensure to use the correct syntax for your operating system
    otpkeysfile.write(str(i))
    otpkeysfile.write("::")
    otpkeysfile.write(otpadkey)
    otpkeysfile.write(",\n")
    otpkeysfile.close()
    
    otpadkey = [] # extremely important to reset this to an empty list 

