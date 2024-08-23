# -*- coding: utf-8 -*-
"""
@author: wraithrune

Dataset 1 - Data Overview - Text Summary

Load in Pre-Processed Data: population_by_country_2020.csv

Reference
1.	Population by Country – 2020: https://www.kaggle.com/datasets/tanuprabhu/population-by-country-2020?resource=download 

Using Pandas Library
"""

# Step 1 - Import Pandas Library
import pandas as pd

# Step 2 - Load the dataset
vFilePath = '../0_Dataset/population_by_country_2020.csv'
vDataFrame = pd.read_csv(vFilePath)

# Step 3 - Data Overview
print("---------------------- Data Overview ----------------------")
print("")
print("---------------- Population by Country 2020 ----------------")

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
