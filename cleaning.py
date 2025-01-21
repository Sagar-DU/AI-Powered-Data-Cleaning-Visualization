print ("Bismillah ArRahmanir Rahim!")
print ("Processing the dataset...")

import pandas as pd

#Load the dataset
# df = pd.read_csv("Raw files/messy_dataset.csv")
#My written code
df = pd.read_csv ("Raw files/messy_dataset.csv")


#Display the first 5 rows of the dataset    
# print(df.head())
#My written code
# print (df.head())

#Remove duplicate rows
# df.drop_duplicates(inplace=True)
#My written code
df = df.drop_duplicates()

#Standardize text (Names & Departments)
df['Name'] = df['Name'].str.title()
df['Department'] = df['Department'].str.title()

#Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

#Fix Salary Formatting
df["Salary"] = df["Salary"].replace("[\$,]", "", regex=True).astype(float)

#Standardize Date Format
def parse_date(date_str):
    if pd.isna(date_str):
        return pd.NaT
    
    formats = [
        '%Y-%m-%d',    # 2023-12-31
        '%d-%m-%Y',    # 31-12-2023
        '%m-%d-%Y',    # 12-31-2023
        '%Y/%m/%d',    # 2023/12/31
        '%d/%m/%Y',    # 31/12/2023
        '%m/%d/%Y',    # 12/31/2023
        '%b %d, %Y',   # Dec 31, 2023
        '%B %d, %Y'    # December 31, 2023
    ]
    
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    return pd.NaT

# Print original problematic values
# print("Original date values:")
# print(df["Join_Date"].head())

# Apply the date parser
df["Join_Date"] = df["Join_Date"].apply(parse_date)

# Print results after conversion
# print("\nConverted date values:")
# print(df["Join_Date"].head())

# print (df.head())

#Save the cleaned dataset
df.to_csv("Cleaned_dataset.csv", index=False)
print("✅ Data Cleaning Completed! File saved as cleaned_dataset.csv")
