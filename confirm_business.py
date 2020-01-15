#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:03:31 2020

@author: natewagner
"""

from google import google
import usaddress


def getBusinessAddress(business_name, num_page):
    
    """
    This program takes in a business name, 
    runs a google search, 
    then extracts every address associated with 
    that business name, stores them in a dictionary,
    and returns that dictionary
    
    """

    num_page = int(num_page)

    # construct query
    name = str(business_name)
    location_string = 'Manatee County'    
    address_string = 'address'
    
    # Final Query
    query = name + location_string + address_string
    
    
    # Search "Final Query" in Google
    search_results = google.search(query, num_page)
    
    # Parse search results to extract address
    google_results = []
    for result in search_results:
        google_results.append(usaddress.parse(result.description))
        

    # Extract address information
    address = []
    address_book = {}
    cnt = 0
    for item in google_results:
        for parsed_info in item:
            if parsed_info[1] != 'Recipient':
                address.append(parsed_info[0])
                address.append(' ')
        if len(address) != 0:
            if len(address_book) == 0:
                address = ''.join(map(str, address))
                address_book.update( {'Address' : address} )
                address = []
            else:
                cnt += 1
                address = ''.join(map(str, address))
                newkey = 'Address' + str(cnt)
                address_book.update( {newkey : address} )
                address =[]
                
    
    if len(address_book) == 0:
        return 'Could not find an address'
    else:
        return address_book
        
            
           
    
    
# test case    
info = getBusinessAddress(business_name = 'Barker Boatworks', num_page = 1)
for key in info:
    print(key)
    print(info[key]) 
    
    

