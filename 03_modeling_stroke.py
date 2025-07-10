# -*- coding: utf-8 -*-
"""
03_modeling_stroke.py
Author: @Thomas Liang

Created a Logistic regression model with scaled numerical variables and encoded 
categorical variables. Used a 80/20 train-test split, classification metrics 
and 5-fold cross validation to evaluate model.
"""

import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
# Load cleaned data
df = pd.read_csv('stroke_data_cleaned.csv')

# Confirm successfully dropped target columns
print(df.info())

# Convert categorical columns to dummy variables for model compatibility

categorical_columns = ['gender', 'ever_married', 'work_type',
                      'Residence_type', 'smoking_status']

numerical_columns = ['age','avg_glucose_level','bmi']


# Create scalar object
scaler = StandardScaler()

# Scale the numerical columns to balance importances of features 
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])


df_model = pd.get_dummies(df, columns = categorical_columns, drop_first=True) 

# Drop redundant columns and the target variable (stroke) and create 
# two dataframes containing feature and target columns
y = df_model['stroke']  # Target variable
x = df_model.drop(columns =['age_group', 'stroke']) # Input variables

# Split data into train-test split 80-20
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123, stratify = y)

# Create the logistic regression model and fit with the training data.
# makes the logistic regression object balanced to make prediction not bias
model = LogisticRegression(max_iter = 1000, class_weight = 'balanced')  



# Fit the data with training data and creates the model predictor
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Classification report and confusion matrix to check how well our model did
# Model good at detecting strokes, 0.84 recall but has low precision of 0.13
# which means there are a lot of false positives.
# No stroke precision is high but recall is low, so may miss no-stroke cases.
print(classification_report(y_test, y_pred))

# 702 True Negative | 270 False Position | 8 False Negative | 42 True Positive
print(confusion_matrix(y_test, y_pred))

# Used cross validation to get an average f1 score across 5 folds
# F1 score of 0.2266 low score 

cv_seed = StratifiedKFold(n_splits=5, shuffle = True, random_state = 123)
m1_scores = cross_val_score(model, x, y, cv = cv_seed , scoring = 'f1') 

print(f"Mean F1 across 5 folds: {m1_scores.mean():.4f}")
