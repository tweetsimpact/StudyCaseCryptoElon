# using pandas and pyplot
import pandas as pd
import matplotlib.pyplot as plt

headers = ['Date', 'Age', 'Marks']

btc = pd.read_csv() #just scrathing


#using plotpy and yfinance best for stock prices

import yfinance
import plotly.graph_objects as go

tsla1year = yfinance.Ticker('db/TSLA_1year')
hist = tsla1year.historiy(period = '1y')

fig = go.Figure(data=go.Scatter(x=hist.index,y=hist['Close'], mode='lines'))
fig.show()