#wrong data: its only a wrong data.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
print(rohan.to_string())

#here we will set Duration = 45 in row 7.

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
rohan.loc[7,'Duration'] = 45
print(rohan.to_string())

# for larger dataset: now here we will loop through all the values in Duration column, if the value is higher than 120 then set it to 120

import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
for i in rohan.index:
    if rohan.loc[i, "Duration"] > 120 :
        rohan.loc[i,"Duration"] = 120

        print(rohan.to_string())

# you can also remove the rows for the wrong data in larger dataset
import pandas as pd
rohan = pd.read_csv('dirtydata.csv')
for i in rohan.index:
    if rohan.loc[i, "Duration"] > 120 :
       rohan.drop(i, inplace=True)
       
       print(rohan.to_string())

