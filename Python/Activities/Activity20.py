import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter


dataframe = pd.read_excel("Sample.xlsx", sheet_name="Sheet1")
print("Read data from created excel file : \n",dataframe)

print("Numbre of Rows and Columns in the excle file : ",dataframe.shape)
print("Data under Email columns: \n ", dataframe["Email"])

print ("Based on FirstName sorted order :\n",dataframe.sort_values("FirstName"))