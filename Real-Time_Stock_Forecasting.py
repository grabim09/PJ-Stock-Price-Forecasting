#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


# In[2]:


st.title('Real-Time Stock Price Forecasting')


# In[3]:


# Read and print the stock tickers that make up S&P500
tickers_data = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers_data.head())


# In[4]:


tickers_symbol = tickers_data.Symbol.to_list()
tickers_name = tickers_data.Security.to_list()


# In[5]:


tuples = [(idx,(sym, name)) for idx, (sym, name) in enumerate(zip(tickers_symbol, tickers_name))]
tickers = dict(tuples)
# tickers


# In[6]:


TC = pd.DataFrame(tickers).T
TC.columns = ['Symbol', 'Name']
TC['Symbol - Name'] = TC['Symbol'] + ' - ' + TC['Name']
# TC


# In[7]:


chosen_ticker_sn = st.selectbox("Please select available ticker below!",TC['Symbol - Name'])
st.write('You have chosen ' + chosen_ticker_sn + ' Tickers')
# chosen_ticker_sn = 'ACN - Accenture'
chosen_ticker_symbol = TC.loc[TC['Symbol - Name'] == chosen_ticker_sn, 'Symbol'].item()
# chosen_ticker_symbol


# In[10]:


stock_data = yf.download(tickers = chosen_ticker_symbol,period='7d',interval='5m')
st.dataframe(stock_data, height = 300, use_container_width = True)
# stock_data = yf.download(tickers = 'GOOGL',period='7d',interval='5m')
# stock_data


# In[9]:


stock_data['Adj Close'].plot()
plt.show()
fig = plt.figure(figsize=(8,4))
st.pyplot(fig) # instead of plt.show()

