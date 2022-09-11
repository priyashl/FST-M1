# Import pandas
import pandas as pd

# Create a Dictionary that will hold our data
data = {
  "Usernames": ["admin", "Charles", "Deku"],
  "Passwords": ["password", "Charl13", "AllMight"],
  "Location": ["Pune","Gurgaon", "Delhi"] 
}

# Create a DataFrame using that data
dataframe = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame : \n",dataframe)

"""
 Write the DataFrame to a CSV file
 To avoid writing the index numbers to the file as well
 the index property is set to false
"""
dataframe.to_csv("sample.csv", index=False)