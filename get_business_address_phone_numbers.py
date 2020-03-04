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
    
    #print(google_search)
    
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
        return business_info[0], business_info[2]
    
    return business_info[0], business_info[2]

    
    
    

#get_business_address_phone_numbers("Bradenton EDC")





data = pd.read_csv("/Users/natewagner/Documents/EDC/hoovers_targeted_industry_with_industrysec.csv")
data.columns

data1 = data[0:500]
data2 = data[500:1000]
data3 = data[1000:1500]
data4 = data[2000:2500]
data5 = data[2500:3000]
data6 = data[3000:3500]
data7 = data[3500:4000]
data8 = data[4000:4500]
data9 = data[4500:5000]
data10 = data[5000:5500]
data11 = data[5500:6000]
data12 = data[6000:6500]
data13 = data[6500:7000]
data14 = data[7000:7500]
data15 = data[7500:7827]



def getinfo(df, outputfile):

    # extract needed columns   
    comp_names = df['companyname']    
    comp_names = list(comp_names)    
    # loop through each business and run the program
    business_addresses = []
    business_phone_numbers = []

    for line in range(0,len(comp_names)):
        name = comp_names[line]
        business_address, business_phone_number = get_business_address_phone_numbers(str(name))
        business_addresses.append(business_address)
        print(business_phone_number)
        if business_phone_number != False:
            if "-" not in business_phone_number:
                business_phone_numbers.append(False)
            else:
                business_phone_numbers.append(business_phone_number)
        else:
            business_phone_numbers.append(False)
        #print(business_addresses[line])
        print(line)
     
    
    
    data1 = df.copy()
    data1['business_addresses'] = business_addresses
    data1['business_phone_numbers'] = business_phone_numbers
    data1.business_addresses.value_counts()
    data1.business_phone_numbers.value_counts()
    
    data1.to_csv('/Users/natewagner/Documents/EDC/' + str(outputfile), encoding='utf-8')


#getinfo(data1, "hoovers_targeted_with_nums_data1.csv")
#getinfo(data2, "hoovers_targeted_with_nums_data2.csv")
#getinfo(data3, "hoovers_targeted_with_nums_data3.csv")
#getinfo(data4, "hoovers_targeted_with_nums_data4.csv")
#getinfo(data5, "hoovers_targeted_with_nums_data5.csv")
#getinfo(data6, "hoovers_targeted_with_nums_data6.csv")
#getinfo(data7, "hoovers_targeted_with_nums_data7.csv")
#getinfo(data8, "hoovers_targeted_with_nums_data8.csv")
#getinfo(data9, "hoovers_targeted_with_nums_data9.csv")
#getinfo(data10, "hoovers_targeted_with_nums_data10.csv")
#getinfo(data11, "hoovers_targeted_with_nums_data11.csv")
#getinfo(data12, "hoovers_targeted_with_nums_data12.csv")
#getinfo(data13, "hoovers_targeted_with_nums_data13.csv")
#getinfo(data14, "hoovers_targeted_with_nums_data14.csv")
#getinfo(data15, "hoovers_targeted_with_nums_data15.csv")





