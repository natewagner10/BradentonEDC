#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:57:08 2020

@author: natewagner
"""

#import usaddress
from bs4 import BeautifulSoup
import requests
import pandas as pd




def get_business_address_phone_numbers(business_name):

    search = ''
    for string in business_name.split():
        search += str(string)
        search += '+'



    begenning_of_search = 'https://www.google.com/search?q='
    google_search = begenning_of_search + search
    
    print(google_search)
    
    page = requests.get(str(google_search))
    
    soup = BeautifulSoup(page.text, 'html.parser')
    
    company_data_from_google = soup.find_all('span', {'class':'BNeawe tAd8D AP7Wnd'})

    business_info = []
    for line in company_data_from_google:
        business_info.append(line.text)
        
    if len(company_data_from_google) == 0:
        return False, False
    
    if len(company_data_from_google) == 1:
        return business_info[0], False
    
    if len(company_data_from_google) == 2:
        return business_info[0], business_info[1]
    
    if len(company_data_from_google) > 3:
        return "BROKE", "BROKE"
    
    return business_info[0], business_info[2]

    
    
    

#get_business_address_phone_numbers("Bradenton EDC")





data = pd.read_csv("/Users/natewagner/Documents/EDC/NewCollegeDataProject.csv")
data.columns

# extract needed columns   
comp_names = data['Company Name']    

# loop through each business and run the program
business_addresses = []
business_phone_numbers = []

for line in range(0,len(comp_names)):
    name = comp_names[line]
    business_address, business_phone_number = get_business_address_phone_numbers(str(name))
    business_addresses.append(business_address)
    business_phone_numbers.append(business_phone_number)
    print(business_addresses[line])
    print(line)
    


data1 = data.copy()
data1['business_addresses'] = business_addresses
data1['business_phone_numbers'] = business_phone_numbers
data1.business_addresses.value_counts()
data1.business_phone_numbers.value_counts()




281/471













