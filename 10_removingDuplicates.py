# removing the duplicate values: 1st you need to discover the duplicate values via duplicated() method

# loading and reading the original dataframe
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
print(rohan.to_string())


# return true for every row that is duplicate otherwise return false:
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
print(rohan.duplicated())

# removing the duplicate from the data set. via drop_duplicates()
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan.drop_duplicates(inplace=True)
print(rohan.to_string())
