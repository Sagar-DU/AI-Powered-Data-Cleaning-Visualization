print ("Bismillah ArRahmanir Rahim")

import pandas as pd

#Load the dataset
df = pd.read_csv("Raw files/messy_dataset.csv")

#Display the first 5 rows of the dataset    
print(df.head())

#Clean the dataset
# df.dropna(inplace=True)

#Remove duplicate rows
df.drop_duplicates(inplace=True)

#Display the first 5 rows of the dataset    
print(df.head())


