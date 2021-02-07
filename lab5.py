#!/usr/bin/env python
# coding: utf-8
#  lab5.py
#  Lab instruction: run the givencode (to do Task#0 & #1, then proceed to uncomment more lines in each next task section)
#  
#
#
#importing libraries
import pandas as pd
import numpy as np

#Read csv file inot a panda dataframe
df = pd.read_csv("c:/Users/User10/Desktop/property data.csv")

#------ Task#0 -- Looking at the given 9 rows 
print (df.head(9))
print ("===== End Task#0 ======")

#------ Task#1 -- Looking at the ST_NUM column and check if there are missing data (standard forms)
#   ... if isnull() is TRUE --> we found one standard missing value
print (df['ST_NUM'])
print (df['ST_NUM'].isnull())
print ("===== End Task#1 ======")


#------ Task#2 -- Looking at the NUM_BEDROOMS column and check if there are missing data (non-standard forms)
#------Note --- Pandas's standard isnull() method can only detect 1 standard missing values, but fail to detect 3 more here 
#print (df['NUM_BEDROOMS'])
#print (df['NUM_BEDROOMS'].isnull())
#print ("===== End Task#2 ======")


# ------ Task#3 --------- Modify the read csv file codes at the top section with the below codes, then do Task#2 again, observe
#------------------------- the correct output now with a total of 4 missing values in the NUM_BEDROOMS column
# Making a list of missing value types
# missing_values =["n/a", "na", "--"]
# df = pd.read_csv("c:/Users/User10/Desktop/property data.csv", na_values = missing_values)
# print ("==== End Task#3 ==========")


#------ Task#4 -- Looking at the OWN_OCCUPIED column and check if there are missing data 
#                 (i.e.integer values in place of  string Y/N)
# Looking at the given OWN_OCCUPIED column
#print (df['OWN_OCCUPIED']
#print (df['OWN_occupied'].isnull()
#print ("--------- shown original OWN_OCCUPIED ------------")
# Detect numbers in the string column
#cnt=0
#for row in df['OWN_OCCUPIED']:
#    try:
#        int(row)
#        df.loc[cnt, 'OWN_OCCUPIED']=np.nan
#    except ValueError:
#        pass
#    cnt+=1
#print (df['OWN_OCCUPIED']
#print (df['OWN_occupied'].isnull())
#print ("--------- shown after handling OWN_OCCUPIED missing data of an integer------------")
#print ("==== End Task#4 ==========")



#------ Task#5 -- Find Total count of missing data cells in each column -------------
print (df.isnull().sum())
#print ("==== End Task#5 ==========")
# In[ ]:




