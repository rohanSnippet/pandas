# DataFrame; it is a 2D data structure like a 2D array with tables including rows and columns.
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
rohan = pd.DataFrame(data)
print(rohan)

# Locate row : pandas use the loc attribute to return one or more specified row.

import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
rohan = pd.DataFrame(data)
print(rohan.loc[0])

# example of returning row 0 and 1
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
rohan = pd.DataFrame(data)
print(rohan.loc[[0,1]])

# named index: with the index arg, you can name your own index
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
rohan = pd.DataFrame(data, index=["day1","day2","day3"])
print(rohan)

# locate the named indexes:
import pandas as pd
data = {"cal":[420,380,390],"dur":[50,40,45]}
rohan = pd.DataFrame(data, index=["day1","day2","day3"])
print(rohan.loc[["day1","day2"]])

# load the data from the csv file into dataframe i.e. data.csv

import pandas as pd
fileload = pd.read_csv('data.csv')
print(fileload)