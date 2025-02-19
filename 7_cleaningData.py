# cleaning data : it means fixing the bad data in your data set. 
#Bad data could be : empty cell, data in a wrong format, duplicate data and wrong data. 

#empty cell: it will give you wrong result always, we will have to remove the rows always that contains thte bad data.

# loading and reading the og dataframe
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
print(rohan.to_string())

#here we will return a new data frame with no empty cell.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohannew = rohan.dropna()
print(rohannew.to_string())

#### If at any case you want to change the og dataframe , then use the inplace = True argument. It will remove the rows containing the NULL(NaN) values.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan.dropna(inplace=True)
print(rohan.to_string())


# replacing the empty value: we will use the fillna() method, which will allow us to replace the empty cell with a value.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan.fillna(130, inplace=True)
print(rohan.to_string())

# to replace only the empty value for the one column, you need to specify the column name

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan["Calories"].fillna(130,inplace=True)
print(rohan.to_string())

# we can also replace the empty cell using mean(), median() or mode().
# calculate the mean and replace the empty values with it.
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
x = rohan['Calories'].mean()
rohan['Calories'].fillna(x,inplace=True)
print(rohan.to_string())

# calculate the median and replace the empty values with it.
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
x = rohan['Calories'].median()
rohan['Calories'].fillna(x,inplace=True)
print(rohan.to_string())

# calculate the mode and replace the empty values with it.
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
x = rohan['Calories'].mode()[0]
rohan['Calories'].fillna(x,inplace=True)
print(rohan.to_string())