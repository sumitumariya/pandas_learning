# Difference between csv file and excel file format:-
# CSV:-> Csv format is a plain text format in which values are seperated by commas(comma seperated values).
# Xls:-> Xls file format is an excel sheets binary file format which holds in formation about all the worksheets in a file ,including both content and formatting.

# write csv file:->

import pandas as pd
dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
d=pd.DataFrame(dis)
print(d)

# d.to_csv("Test_new.csv")  #create csv file (visible in same folder)
# d.to_csv("test_new1.csv",index=False)  #if we doesn't want indexing 

# change head data
d.to_csv("test_new2.csv",index=False,header=[1,2,3]) 
# No head data
d.to_csv("test_new3.csv",header=False)# if we don't want header
