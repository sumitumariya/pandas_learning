# functions of pandas

import pandas as pd   

csv_1=pd.read_csv("C:\\Users\\Lenovo\Downloads\\day.csv")

# print(csv_1)

# print(csv_1.index) #show index
# print(csv_1.columns)#show columns


# describe function.....................
# print(csv_1.describe())

# output of describe function

#          Numeric  Numeric-2
# count  31.000000  31.000000
# mean   16.000000  16.000000
# std     9.092121   9.092121
# min     1.000000   1.000000
# 25%     8.500000   8.500000
# 50%    16.000000  16.000000
# 75%    23.500000  23.500000
# max    31.000000  31.000000
# .........................................................
# Head function :-
# a=csv_1.head()
# a=csv_1.head(2) #shows 2 data 
# print(a)

# output:-> top five data
#   Numeric  Numeric-2 Numeric-Suffix
# 0        1          1            1st
# 1        2          2            2nd
# 2        3          3            3rd
# 3        4          4            4th
# 4        5          5            5th
# ............................................................
# Tail function :-bottom five data
# a=csv_1.tail()
# print(a)

# output:-
#   Numeric  Numeric-2 Numeric-Suffix
# 26       27         27           27th
# 27       28         28           28th
# 28       29         29           29th
# 29       30         30           30th
# 30       31         31           31st
# ..........................................................
#  function :-
# a=csv_1[:2] #slicing for particular amount of data
# print(a)
# ....................................................
# print(csv_1.index.array)#convert index number to array
# ....................................................
# a=csv_1.to_numpy()
# print(a) #converted into numpy array
# ...........................................
# assending order
# axis=0 --->according to row
# axis=1 --->according to column
# a=csv_1.sort_index(axis=0,ascending=False)
# print(a) 
# .............................
# show  data of only particular column
# a=csv_1.loc[[1,2],["Numeric"]]
# print(a)
# ...................................
# a=csv_1.iloc[0,2]
# print(a)

# excape column
# a=csv_1.drop("Numeric",axis=1)
# print(a)

