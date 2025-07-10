# -*- coding: utf-8 -*-
'''
02_EDA_stroke.py
Author: @Thomas Liang

Exploratory Data Analysis for the dataset to explore potential
trends, patterns, and relationships between the response variable and 
explanatory variables. Various plots were used to examine, group and address
differences and multicollinearity issues.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv('stroke_data_cleaned.csv')

# Checks statistical description of dataset
print(df.describe(include = 'all')) # All

print(df.describe()) # Numerical 

# Countplot of stroke count 
# Clear inbalance: out of 5109 participants 249 had a stroke while 4860 did not.
stroke_count = sns.countplot (x = 'stroke', data = df)

# Labels and titles
plt.title('Stroke Count')
plt.xlabel ('Stroke (0 = No, 1 = Yes)')
stroke_count.bar_label(stroke_count.containers[0]) # Bar labels above
plt.show()


# Barplot of stroke % by age group
# Stroke risk appears to increase with age, especially 30 years and above.
age_bin_labels = [  #The order displayed
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

age_stroke = sns.barplot(
    x = 'age_group',
    y = 'stroke',
    data = df,
    estimator=lambda x: sum(x)/len(x) * 100, # Calulates % of stroke by age group
    order = age_bin_labels,
    errorbar = None) # Removes confidence interval for visual clarity
    
plt.title('Stroke % by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Stroke')
# Bar labels above and formats to 2 decimal places
age_stroke.bar_label(age_stroke.containers[0], fmt ='%.2f%%') # Bar labels above
plt.show()

# Barplot of stroke % by gender
# There seems to be slight variation in stroke occurrence between genders.
gender_count = sns.barplot(
    x='gender',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by gender
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Gender')
plt.xlabel('Gender')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
gender_count.bar_label(gender_count.containers[0], fmt ='%.2f%%') 
plt.show()

# Barplot of stroke percentage between patients with and without hypertension
# Hypertension appears to be associated with higher likelihood of stroke
hypertension_count = sns.barplot(
    x='hypertension',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by hypertension
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Hypertension ')
plt.xlabel('Hypertension (0 = No, 1 = Yes')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
hypertension_count.bar_label(hypertension_count.containers[0], fmt ='%.2f%%') 
plt.show()


# Barplot of stroke percentage between patients with and without heart_disease
# Heart disease appears to be associated with higher likelihood of stroke
heart_disease_count = sns.barplot(
    x='heart_disease',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by heart_disease
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Heart Disease ')
plt.xlabel('Heart Disease (0 = No, 1 = Yes')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
heart_disease_count.bar_label(heart_disease_count.containers[0], fmt ='%.2f%%') 
plt.show()

# Barplot of stroke percentage between patients with different smoking status
# Smoking appears to be associated with higher likelihood of stroke
smoking_status_count = sns.barplot(
    x='smoking_status',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by smoking status
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
smoking_status_count.bar_label(smoking_status_count.containers[0], fmt ='%.2f%%') 
plt.show()


# Barplot of stroke percentage by marital status
# Being married does appear to be associated with higher likelihood of stroke
married_count = sns.barplot(
    x='ever_married',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by marital status
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Marital Status')
plt.xlabel('Married')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
married_count.bar_label(married_count.containers[0], fmt ='%.2f%%') 
plt.show()

# Barplot of stroke percentage by work type
# Work type does appear to have be associated with stroke occurrence
work_count = sns.barplot(
    x='work_type',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by work type
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Work Type')
plt.xlabel('Work Type')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
work_count.bar_label(work_count.containers[0], fmt ='%.2f%%') 
plt.show()

# Barplot of stroke percentage by residence type
# There seems to be slight variation in stroke occurrence between resident types
residence_count = sns.barplot(
    x='Residence_type',
    y='stroke', 
    data=df, 
    estimator=lambda x: sum(x)/len(x) * 100, # Calculates % of stroke by residence type
    errorbar = None) # Removes confidence interval for visual clarity

# Labels and titles
plt.title('Stroke % by Residence Type')
plt.xlabel('Residence Type')
plt.ylabel('Stroke %')
# Bar labels above and formats to 2 decimal places
residence_count.bar_label(residence_count.containers[0], fmt ='%.2f%%') 
plt.show()

# Boxplot of average glucose levels by stroke status
# Stroke group appears to have a higher median than non-stroke group
# Non-stroke group appears to have much more outliers
# Glucose levels of stroke group show greater variability
# Both groups appear to have a positive skew
sns.boxplot(x = 'stroke',  y = 'avg_glucose_level', data = df)

# Labels and titles
plt.title('Glucose Levels by Stroke Status')
plt.xlabel('Stroke (0 = No, 1 = Yes)')
plt.ylabel('Average Glucose Level')
plt.show()

# Boxplot of BMI by stroke status
# Stroke group appears to have a higher median BMI than non-stroke group
# Non-stroke group appears to have much more outliers, mostly upper outliers
# BMI of non-stroke group show greater variability
# No clear skew in either groups
sns.boxplot(x = 'stroke',  y = 'bmi', data = df)

# Labels and titles
plt.title('BMI by Stroke Status')
plt.xlabel('Stroke (0 = No, 1 = Yes)')
plt.ylabel('BMI')
plt.show()

# Boxplot of Age by stroke status
# Stroke group median age is much higher.
# Stroke group appears to have more outliers, lower outliers
# Age of non-stroke group show greater variability
# No clear skew in no stroke group, lower skew in stroke group
sns.boxplot(x = 'stroke',  y = 'age', data = df)

# Labels and titles
plt.title('Age by Stroke Status')
plt.xlabel('Stroke (0 = No, 1 = Yes')
plt.ylabel('Age')
plt.show()

# Correlation Matrix to reveal pairwise relationships among the numerical variables
# No strong correlation between any two variables. All correlations are below 0.4, 
# which suggest no strong linear relationships between the numerical variables. 
# There appears to be no serious concern regarding multicollinearity.
# Since most variables have low correlation it suggest stroke risk depends on a 
# combination of factors.
corr_matrix = df.corr(numeric_only = True)
sns.heatmap(corr_matrix, annot=True, cmap='RdBu_r', fmt = '.2f')
plt.title('Correlation Matrix')
plt.show()

