#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:56:35 2020

@author: natewagner
"""

import re
from google import google
import pandas as pd



line = "Barker Boatworks. Address: 7910 25th Court Street East Suite 115. Sarasota, Fl 34243. Kevin Barker. 941-232-8646 · kevin@barkerboatworks.com. Name."
match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
match





def getEmail(business_name, city, num_page, title_info = False):
    
    """
    This program takes in a business name, 
    runs a google search, 
    then extracts every address associated with 
    that business name, stores them in a dictionary,
    and returns that dictionary
    
    """
    #current_address = str(current_address)
    num_page = int(num_page)

    # construct query
    name = str(business_name)
    location_string = str(city)
    address_string = ' email address'
    
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
            googles = re.findall(r'[\w\.-]+@[\w\.-]+', result.description)
            if len(googles) != 0:
                google_results.append(googles)
        if title_info == True:
            googles = re.findall(r'[\w\.-]+@[\w\.-]+', result.name)
            if len(googles) != 0:
                google_results.append(googles)
                
    print(google_results)
    if len(google_results) == 0:
        return False
    else:
        return google_results[0][0]
    #print ("LINE BREAK")           
        


        
data = pd.read_csv("/Users/natewagner/Documents/EDC/NewCollegeDataProject.csv")
data.columns
    
comp_names = data['Company Name']    
comp_city = data['Business City']


emails = []
for x in range(0,len(comp_names)):
    name = comp_names[x]
    city = comp_city[x]
    isExists = getEmail(str(name), str(city), 2, title_info = False)
    if isExists == False:
        isExists = getEmail(str(name), str(city), 2, title_info = True)
        emails.append(isExists)
    else:
        emails.append(isExists)
    print (x)

data['emails'] = emails
data.emails.value_counts()
data.to_csv('/Users/natewagner/Documents/EDC/currentWithEmails.csv', encoding='utf-8')


cntt = 0
for x in emails:
    if x == False:
        cntt += 1
print (cntt)



getEmail(business_name = 'Spectrum Custom Molds', city = 'Bradenton', num_page = 2, title_info=False)

comp_names[0]












