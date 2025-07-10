# Stroke Data Analysis and Modeling

### Overview
- This project aims to analyze health and demographic data to further understand factors associated with stroke occurrence. It contains initial data cleaning and preprocessing, exploratory data analysis, and the creation of a logistic regression model to predict likelihood of stroke.


### Dataset 

- **Source**: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
- **Description**: The dataset contains health and demographic information for individuals, including attributes such as age, hypertension, heart disease, average glucose level, BMI, and whether they have had a stroke.
- **Target Variable**: 'stroke' (0 = no, 1 = yes)
- **Rows**: 5110 Entries
- **Columns**: 12 variables


### Data Cleaning (01_data_cleaning_stroke.py)
- Checked for missing values and data inconsistencies.
- Created age group bins to capture non-linear relationships between age and stroke.
- Imputed missing 'bmi' values using the average BMI grouped by **gender** and **age** groups.
- Dropped the id column as it is not useful for analysis.
- Dropped the single ''other'' entry in the 'gender' column as it only had 1 entry which could cause problems when creating dummy variables.


### Exploratory Data Analysis (02_EDA_stroke.py)
- Analyzed the class imbalance in the target variable, found that stroke cases made a small percentage of the dataset.
- Created bar plots and box plots to explore relationships between target variable and explanatory variables.
- Identified that work_type, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, and bmi showed noticeable patterns when compared to stroke occurrence.
- Created heatmaps to explore correlation of variables and to discover potential collinearity issues.

### Modeling (03_modeling_stroke.py)
- Performed preprocessing steps including the use of dummy variables for categorical variables and normalized continuous variables.
- Used logistic regression to predict likelihood of stroke based on health and demographic.
- Chose logistic regression because it is suitable for binary classification problems and for its interpretability.
- Addressed class imbalance by setting 'class_weight='balanced'' in the model.
- Split the data into 80/20 training and test sets using stratified sampling to train model and maintain class balance.
- Conducted cross validation, which returned a average f1 score of 0.227 across 5 folds.

### Key Findings
- Stroke cases in the study accounted for 4.9% of cases, displaying clear class imbalance.
- Achieved a high recall of 0.84 but low precision of 0.13. This suggests that the model correctly identifies strokes at a high rate, but also has a high rate of false positives.
- Older age groups showed significantly higher stroke incidence. 


### How to Run
1. Download the dataset
2. Run '01_data_cleaning_stroke.py' to clean and prepare the data.
3. Run '02_EDA_stroke.py' to perform exploratory data analysis and generate visuals.
4. Run '03_modeling_stroke.py' to train the logistic regression model and evaluate performance.


### Environment and Packages Used
- python 3.11.12
- pandas 2.2.3
- scikit-learn 1.7.0
- matplotlib 3.10.3
- seaborn 0.13.2
