import sys
import os
import shutil
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shutil import copyfileobj
from collections import Counter

ColumnNumber = 2
ColumnData = []
counter = 0
global namecounter
word = "name"
list_of_countries = ["AGO", "BDI", "BEN", "BFA", "BWA", "CAF", "CIV", "CMR", 
                     "COD", "COG", "MAR", "DZA", "DZ", "ZAF", 'MUS', 'CPV', 
                     'TUN', 'ETH', 'SYC', 'MDG', 'NGA', 'COD', 'UGA', 'KEN', 
                     'LBY', 'SDN', 'ZWE', 'TZA', 'MLI', 'GHA', 'CMR', 'ERI', 
                     'SEN', 'REU', 'BFA', 'CIV', 'LBR', 'NAM', 'AGO', 'SOM', 
                     'RWA', 'MOZ', 'TCD', 'NER', 'GIN', 'GMB', 'GAB', 'TGO',
                     'DJI', 'MRT', 'MR', 'BWA', 'SLE', 'BEN', 'ZMB', 'MWI', 
                     'BDI', 'SSD', 'SS', 'LSO']
# list of (hopefully) all the country abbreviations in the file(s)

victordir = "C:\\Users\\Victor\\Desktop\\scraped"
krishnadir = "C:\\Users\\krishna\\Downloads\\myfiles"
# everyone's directories for the scraped folders so we don't have to retype it
iterator = 0
files = os.listdir(victordir)
for file in files:
    with open(victordir + "\\" + file, 'r') as f:
        for country_name in list_of_countries:
            if country_name in f.read():
                specific_dir = country_name + str(iterator)
                os.makedirs(specific_dir)
                iterator += 1
                #f.write(country_name + str(namecounter) + "file")
                local_file = open(specific_dir, "w")
                local_file.write(f)
                




            '''
            if "name" in line_txt:
                counter += 1
                print("location name found @ ", counter)
                words = line_txt.split()
                for i in words:
                    if(i==word):
                        namecounter +=1
    namecounter += 0
    print("count of name ", namecounter)
        '''

'''
def organize_files():
    os.makedirs("Master Directory")
    with open("C:\\Users\\...") as g:
        
        
        


get_country_name()
organize_files()
'''

'''
with open("C:\\Users\krishna\Downloads\TestFile.txt",'r') as file_txt:

    head, tail = os.path.split(file_txt.name)

    print("file name is --> name:" , tail, "   path:",  head)

    file_bkp = open(head + "\\" + tail + ".csv", "w")

    copyfileobj(file_txt, file_bkp)

    for line_txt in file_txt:

        if "name" in line_txt:

            counter += 1

            print("name found @ " , counter)

file_txt.close

file_bkp.close

print(ColumnData)
'''