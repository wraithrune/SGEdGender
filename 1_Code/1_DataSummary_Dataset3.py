# -*- coding: utf-8 -*-
"""
@author: wraithrune

Dataset 3 - Data Overview - Text Summary

Load in Pre-Processed Data: EnrolmentPreUniversitybyLevelandCourse_processed.csv

Reference
1.	Enrolment at Pre-University by Level and Course: https://beta.data.gov.sg/datasets?topics=education&query=jc&resultId=d_a27483941350c79947ebac7803df48d7

Using Pandas Library
"""

# Step 1 - Import Pandas Library
import pandas as pd

# Step 2 - Load the dataset
vFilePath = '../0_Dataset/EnrolmentPreUniversitybyLevelandCourse_processed.csv'
vDataFrame = pd.read_csv(vFilePath)

# Step 3 - Data Overview
print("---------------------- Data Overview ----------------------")
print("")
print("---------------- Enrolment Pre-University by Level and Course ----------------")

print("This is the shape of the dataset")
print(vDataFrame.shape)

print("\nThis is the index of the dataset")
print(vDataFrame.index)

print("\nThese are the columns in the dataset")
print(vDataFrame.columns)

print("\nThe total number of non-NA values in this dataset is:")
print(vDataFrame.notna().sum())

print("\nA summary of this dataset is shown below:")
vDataFrame.info()

print("\nA descriptive statistical summary of this dataset is shown below:")
print(vDataFrame.describe())
