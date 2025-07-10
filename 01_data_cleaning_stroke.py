# -*- coding: utf-8 -*-
'''
01_data_cleaning_stroke.py
Author: @Thomas Liang

Loads the stroke predictor data and performs data cleaning, 
creates bins for age, and saves the cleaned data for analysis. 
'''

import pandas as pd

# Loads raw data
df = pd.read_csv('healthcare-dataset-stroke-data.csv')


# Display basic info of the dataset for initial analysis
print (df.head()) # Displays first 5 rows
print(df.shape) # 5110 rows & 12 columns
print(df.info()) # Displays data types
print(df.isnull().sum()) # Displays the columns with missing values & the count


# Checks max and min age to prepare for age binning
print(df['age'].max())  
print(df['age'].min())  


# Create the bins and labels for age (left-inclusive & right-exclusive)
age_bins = list(range(0, 91, 10))

age_bin_labels = [
    '0-9',
    '10-19',
    '20-29',
    '30-39',
    '40-49',
    '50-59', 
    '60-69',
    '70-79',
    '80-89'
    ]

# Creates new column age_group into dataframe binning ages into 10 year intervals
# and orders them.
df['age_group'] = pd.cut(df['age'], bins = age_bins, labels = age_bin_labels, right = False)
df['age_group'] = pd.Categorical(df['age_group'], categories = age_bin_labels, ordered = True)

# Imputes the missing data in the bmi column by using mean of gender + age_group
df['bmi'] = df.groupby(['gender', 'age_group'], observed = False)['bmi'].transform(lambda x: x.fillna(x.mean()))

# Confirm the values were imputed correctly, there are now 0 missing values.
print(df.info()) 


# Checked distribution of values in the gender column and decided to drop the
# 'other' value as it appears only once, which is not statistically 
# significant enough and may cause issues with group analysis and plots 
df['gender'].value_counts()
df = df[df['gender'] != 'Other']
print(df.info()) 

# Drop unused column id since it will not be useful for analysis
df.drop('id', axis=1, inplace=True)

# Saves cleaned data
df.to_csv('stroke_data_cleaned.csv', index = False)
