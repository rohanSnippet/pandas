# a pandas series is like a column in a table. it is 1D array which holds data of any type.
# here we will create a simple pandas series.

import pandas as pd

rohan = [10,20,30]
rohannew = pd.Series(rohan)
print(rohannew)

# labeling-  label can be used to access a specified value

import pandas as pd
rohan = [10,20,30]
rohannew = pd.Series(rohan)
print("2nd element is : ",rohannew[1])

# with Create label you can create your own name labels:

import pandas as pd
rohan = [1,7,2]
rohannew = pd.Series(rohan, index=["x","y","z"])
print(rohannew)

# labeling-  label can be used to access a specified value(after creating own label)

import pandas as pd
rohan = [10,20,30]
rohannew = pd.Series(rohan, index=["x","y","z"])
print(rohannew['x'])

# you can also use a key or value obj like a dictonary, when creating a series.
# here we'll create a simple pandas series from a dictonary

import pandas as pd
cal = {"day1":420, "day2":380,"day3":390}
rohannew = pd.Series(cal)
print(rohannew)

# now we'll  create a series using only data from day1 and day2

import pandas as pd
cal = {"day1":420, "day2":380,"day3":390}

result = pd.Series(cal, index =["day1","day2"])

print(result)

# DataFrame: Data sets in pandas are usually multidimensional tables, and they are called DataFrames.
# Series are like columns and dataframes is the whole table.

# we will create a dataframe from 2 series.
import pandas as pd
rohan = {"cal":[420, 380, 390], "duration":[50,40,45]}

rohannew = pd.DataFrame(rohan)
print(rohannew)
print('')

# after indexing
rohannew1 = pd.DataFrame(rohan,index=["a","b","c"])
print (rohannew1)