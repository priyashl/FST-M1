import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

## by Debashish on 27th Oct 2021


data = {"FirstName":["Satvik", "Avinash","Lahri"],
    "LastName": ["Shah", "Kati","Rath"],
    "Email": ["satshah@example.com","avinashk@example.com","lahri.rath@example.com"],
    "PhoneNumber": ["4537829158","5892184058","4528727830"]
}
dataframe = pd.DataFrame(data)
print("printing dataframe value : \n",dataframe)


# Create an ExcelWriter object
writer = ExcelWriter("Sample.xlsx")

# Write the DataFrame to the Excel file
dataframe.to_excel(writer, "Sheet1", index=False)

# Save the file
writer.save()


print("-----------------------------------------------------######################################-------------------------------------------")
## read created excel file :


dataframe1 = pd.read_excel("Sample.xlsx", sheet_name="Sheet1")
print("Read data from created excel file : \n",dataframe1)




