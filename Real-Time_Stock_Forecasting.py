#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import streamlit as st


# In[2]:


st.title('Real-Time Stock Price Forecasting')


# In[3]:


# Read and print the stock tickers that make up S&P500
tickers_data = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers_data.head())


# In[6]:


tickers_symbol = tickers_data.Symbol.to_list()
tickers_name = tickers_data.Security.to_list()


# In[11]:


tuples = [(idx,(sym, name)) for idx, (sym, name) in enumerate(zip(tickers_symbol, tickers_name))]
tickers = dict(tuples)
# tickers


# In[18]:


TC = pd.DataFrame(tickers).T
TC.columns = ['Symbol', 'Name']
TC['Symbol-Name'] = TC['Symbol'] + ' - ' + TC['Name']
# TC


# In[19]:


chosen_ticker = st.selectbox("Please select available ticker below!",TC['Symbol-Name'])


# In[20]:


stock_data = yf.download(tickers=chosen_ticker,period='7d',interval='5m')
stock_data


# In[8]:


data['Adj Close'].plot()
plt.show()

