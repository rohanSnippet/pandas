# For the iPhone sales analysis task.

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

rohanData = pd.read_csv('apple_products.csv')
# print(rohanData.isnull().sum())
# print(rohanData.head())
# print(rohanData.describe())
# print(rohanData.columns)
highest_rated= rohanData.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10) 
""" iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
counts = highest_rated['Number Of Ratings'] """

iphone = highest_rated['Product Name'].value_counts()
label = iphone.index
counts = highest_rated['Number Of Reviews']

""" figure = px.bar(highest_rated, x=label, y=counts,  title="Number of reviews of highest Rated Iphones")
# figure.show()
figure.write_html( 'graph.html', auto_open=True ) """

figure = px.scatter(data_frame=rohanData, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship between sale price and number of ratings of iphones")

figure.write_html('graph.html', auto_open=True)
# figure.show()