#!/usr/bin/env python
# coding: utf-8

# In[7]:


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# In[8]:


# Read and print the stock tickers that make up S&P500
tickers = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
print(tickers.head())


# In[10]:


tickers_list = tickers.Symbol.to_list()
tickers_name = tickers.Security.to_list()


# In[13]:


chosen_ticker = st.selectbox("Please select available ticker below!",tickers_name)


# In[5]:


data = yf.download(tickers='GOOGL',period='7d',interval='5m')
data


# In[6]:


data['Adj Close'].plot()
plt.show()

