# Data in wrong format: To fix the problem, there are 2 ways:
# Removing the rows or convert all the cells in the same format.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
print(rohan.to_string())

# lets try to convert all the cells in the date column into dates. to_datetime()

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan["Date"] = pd.to_datetime(rohan['Date'],format="mixed")
print(rohan.to_string())

# here we will remove the rows with a NULL value in the Date columns

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan["Date"] = pd.to_datetime(rohan['Date'], format="mixed")
rohan.dropna(subset=['Date'], inplace=True)
print(rohan.to_string())