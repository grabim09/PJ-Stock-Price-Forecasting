#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# In[2]:


st.title('Real-Time Stock Price Forecasting')


# In[3]:


import yfinance as yf


# In[4]:


# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers.head())


# In[5]:


tickers_list = tickers.Symbol.to_list()
tickers_name = tickers.Security.to_list()


# In[6]:


chosen_ticker = st.selectbox("Please select available ticker below!",tickers_name)


# In[7]:


data = yf.download(tickers='GOOGL',period='7d',interval='5m')
data


# In[8]:


data['Adj Close'].plot()
plt.show()

