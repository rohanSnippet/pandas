#viewing the data: one of the most used method for a quick overview of the dataframe is the head() method. This method returns the headers and a specified number of rows.


#here we will print the 1st 10 rows in the dataframe. 
import pandas as pd
rohan = pd.read_csv('data.csv')
print(rohan.head(10))

#Note: by default rohan.head() without any arg will return first 5 rows.

#here we will print the last 10 rows in dataframe
import pandas as pd
rohan = pd.read_csv('data.csv')
print(rohan.tail(10))

# what if you want the information about data in the dataframe: via info().
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
