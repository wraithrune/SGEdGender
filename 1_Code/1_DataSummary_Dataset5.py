# -*- coding: utf-8 -*-
"""
@author: wraithrune

Dataset Overview - Text Summary

Load in Pre-Processed Data: ITEIntakeEnrolmentandGraduatesbyCourse_processed.csv

Reference
1.	ITE Intake, Enrolment and Graduates by Course: https://beta.data.gov.sg/datasets?topics=education&query=Labour+Force&resultId=d_24b8751abfc87a4f054f61186c2fe1ba
    
Using Pandas Library
"""

# Step 1 - Import Pandas Library
import pandas as pd

# Step 2 - Load the dataset
vFilePath = '../0_Dataset/ITEIntakeEnrolmentandGraduatesbyCourse_processed.csv'
vDataFrame = pd.read_csv(vFilePath)

# Step 3 - Data Overview
print("---------------------- Data Overview ----------------------")
print("")
print("---------------- ITE Intake, Enrolment, and Graduates by Course ----------------")

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
