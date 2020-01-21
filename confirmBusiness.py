#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:03:31 2020

@author: natewagner
"""

from google import google
import usaddress
import stringdist




def getBusinessAddress(business_name, current_address, num_page):
    
    """
    This program takes in a business name, 
    runs a google search, 
    then extracts every address associated with 
    that business name, stores them in a dictionary,
    and returns that dictionary
    
    """
    current_address = str(current_address)
    num_page = int(num_page)

    # construct query
    name = str(business_name)
    location_string = 'Sarasota'    
    address_string = 'address'
    
    # Final Query
    query = name + location_string + address_string
    
    
    # Search "Final Query" in Google
    search_results = google.search(query, num_page)
    
    # Parse search results to extract address
    google_results = []
    for result in search_results:
        #print (result.description)
        google_results.append(usaddress.parse(result.description))
        
        
    neededInfo = ['AddressNumber', 'StreetName', 'StreetNamePostType', 'StreetNamePostDirectional']
        
    # Extract address information
    address = []
    address_book = {}
    cnt = 0
    for item in google_results:
        for parsed_info in item:
            if parsed_info[1] == 'AddressNumber':
                cnt += 1
                if cnt == 2:
                    num = int(len(address_book))
                    newkey = 'Address' + str(num)
                    address = ''.join(map(str, address))
                    address_book.update( {newkey : address} )
                    address = []
                    cnt = 1
            if parsed_info[1] in neededInfo and cnt == 1:
                address.append(parsed_info[0])
                address.append(' ')

    final_address_book = {}
    for key in info:
        lev_dist = stringdist.levenshtein(str(info[key]), current_address)
        if lev_dist < 5:
            final_address_book.update( {key : info[key]})
            
    if len(final_address_book) == 0:
        return address_book
    else:        
        return final_address_book          
                
                
        
           
    
    
# test case    
info = getBusinessAddress(business_name = '24 Seven Enterprises Inc', current_address = '7135 16Th St E', num_page = 1)

for key in info:
    print(key)
    print(info[key])
    
    