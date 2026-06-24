"""Libraries are used to manipulate data and perform various operations without having to write the code from scratch. Python has a rich ecosystem of libraries that can be used for various purposes, such as data analysis, machine learning, web development, and more"""
""" Pandas is a powerful library in Python that is used for data manipulation and analysis. It provides data structures like Series and DataFrame, which are essential for handling and analyzing data efficiently. With pandas, you can easily read and write data from various file formats, perform data cleaning, transformation, and analysis tasks with ease"""
import pandas as pd 
# Creating a DataFrame from a dictionary
data = { # this is a dictionary that contains the data for our DataFrame
    'name' : ["Atharva","Chetan","Amit"],
    'marks' : [None, 50, 90],
    'age' : [19, 20, None]
}
df = pd.DataFrame (data) # this creates a DataFrame from the dictionary
print(df)
# correcting the missing values in the DataFrame
df["marks"]  = df["marks"].fillna(df["marks"].mean()) # fillna() is used to fill the missing values in the "marks" column with the mean of the "marks" column
df["age"] =  df["age"].fillna(df["age"].mean())
# After cleaning 
print(df)
print("Analysis of the DataFrame:")
print(df.describe()) # this will give us a statistical summary of the DataFrame
# exporting the DataFrame to a CSV file
df.to_csv("students_data.csv", index=False) # this will export the DataFrame to a CSV file named "students_data.csv" without the index column
print("Data exported Successfully")
