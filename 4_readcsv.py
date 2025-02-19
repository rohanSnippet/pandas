# read csv files: (comma seperated file) it is a simple way to store the big and biggest data sets. csv files contains plain text. 

# loading the csv into a dataframe with to_string().
# Note: Always use single quotes for importing a csv file to avoid conflicts.

import pandas as pd
df= pd.read_csv('data.csv')
print(df.to_string())

# loading the csv into a dataframe without to_string().

import pandas as pd
df= pd.read_csv('data.csv')
print(df)

# max_rows : to check your system's maximum rows with: 
import pandas as pd
print(pd.options.display.max_rows)

# yes, we can increase the maximum no. of rows to display the entire dataframe.
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
