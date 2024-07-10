# handling missing values (dropna and fillna)in pandas
# dropna--->remove value
# fillna---->without removing fill another data
import pandas as pd

var =pd.read_csv("C:\\Users\\Lenovo\\Downloads\\day.csv")
print(var)
# dropna remove blank places row
# print(var.dropna())

# axis parameter
# print(var.dropna(axis=1))    #axis 1=column (remove whole column)
# print(var.dropna(axis=0))    #axis=0=rows (remove whole row)

# how parameter
# print(var.dropna(how="any"))# remove all nan values
# print(var.dropna(how="all"))# remove all nan rows

# subset parameter
# print(var.dropna(subset=["Numeric-Suffix"])) #remove nan values of given column

# implace parameter
# print(var.dropna(inplace=True))#remove all values and added it to new data

# thresh parameter
# print(var.dropna(thresh=1))#remove single nan value row


