#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 12:03:31 2020

@author: natewagner
"""

from google import google
import usaddress
import stringdist
import pandas as pd



def getBusinessAddress(business_name, current_address, city, num_page, title_info = False):
    
    """
    This program takes in a business name,
    the current address and city on file,
    runs a google search, 
    then extracts every address associated with 
    that business name, stores them in a dictionary,
    and then cross references them with the address on file.
    
    If returned addresses are within a given levenshein
    distance, the program returns True.
    
    """
    current_address = str(current_address)
    num_page = int(num_page)

    # construct query
    name = str(business_name)
    location_string = str(city)
    address_string = ' address'
    
    # Final Query
    query = name + ' ' + location_string + address_string
    #print(query)
    
    # Search "Final Query" in Google
    search_results = google.search(query, num_page)
    
    # Parse search results to extract address

    google_results = []
    for result in search_results:
        #print (result.description)
        if title_info == False:
            google_results.append(usaddress.parse(result.description))
        if title_info == True:
            google_results.append(usaddress.parse(result.name))

        
        
    neededInfo = ['AddressNumber', 'StreetNamePreDirectional', 'StreetName', 'StreetNamePostType', 'StreetNamePostDirectional', 'OccupancyIdentifier']
        
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
    #print(address_book)
    for key in address_book:
        lev_dist = stringdist.levenshtein(str(address_book[key]).rstrip().lower(), current_address.rstrip().lower())
        if address_book[key][0:5] == current_address[0:5]:
            final_address_book.update( {key : address_book[key]})
        if int(lev_dist) <= 10:
            final_address_book.update( {key : address_book[key]})
    #return final_address_book
    if len(final_address_book) == 0:
        return False
    else:        
        return True          
                
                
        
# read in data      
data = pd.read_csv("/Users/natewagner/Documents/EDC/NewCollegeDataProject.csv")
#data.columns
 
# extract needed columns   
comp_names = data['Company Name']    
comp_addresses = data['Business Street']
comp_city = data['Business City']

# loop through each business and run the program
business_exists = []
for x in range(0,len(comp_names)):
    name = comp_names[x]
    street = comp_addresses[x]
    city = comp_city[x]
    isExists = getBusinessAddress(str(name), str(street), str(city), 2, title_info = False)
    if isExists == False:
        isExists = getBusinessAddress(str(name), str(street), str(city), 2, title_info = True)
    business_exists.append(isExists)
    print (x)
    
# create new column in data frame    
data['business_exists'] = business_exists
#data.business_exists.value_counts()

# write to csv
data.to_csv('/Users/natewagner/Documents/EDC/currentWithExists.csv', encoding='utf-8')







# test cases
info = getBusinessAddress(business_name = 'AC Warehouse Bradenton', current_address = '710 60th Street Court E', city = 'Bradenton', num_page = 2, title_info=False)

for key in info:
    print(key)
    print(info[key])
    
    
    
doc = 'See reviews for AC Warehouse in Bradenton, FL at 710 60th St Crt E from Angies List members or join today to leave your own review.'

usaddress.parse(doc)
one = 'PO Box 303 1981 Center Road'
two = '1981 Center Rd'
stringdist.levenshtein(one.rstrip().lower(), two.rstrip().lower())

    