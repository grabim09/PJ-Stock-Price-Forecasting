#!/usr/bin/env python
# coding: utf-8

# In[15]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


# In[16]:


def get_ticker():
    # Read and print the stock tickers that make up S&P500
    tickers_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]


# In[17]:


def choose_ticker():
    tickers_symbol = tickers_data.Symbol.to_list()
    tickers_name = tickers_data.Security.to_list()
    tuples = [(idx,(sym, name)) for idx, (sym, name) in enumerate(zip(tickers_symbol, tickers_name))]
    tickers = dict(tuples)
    # tickers
    tickers_list = pd.DataFrame(tickers).T
    tickers_list.columns = ['Symbol', 'Name']
    tickers_list['Symbol - Name'] = tickers_list['Symbol'] + ' - ' + tickers_list['Name']
    # tickers_list
    chosen_ticker_sn = st.selectbox("Please select available ticker below!",tickers_list['Symbol - Name'])
    chosen_ticker_symbol = tickers_list.loc[tickers_list['Symbol - Name'] == chosen_ticker_sn, 'Symbol'].item()
    stock_data = yf.download(tickers = chosen_ticker_symbol,period='7d',interval='5m')
    stock_data = stock_data.drop((stock_data == 0).any(axis=1))
    st.write('You have chosen ' + chosen_ticker_sn + ' Tickers')
    st.dataframe(stock_data, height = 200, use_container_width = True)
    return stock_data


# In[18]:


stock_data['Adj Close'].plot()
plt.show()
fig = plt.figure(figsize=(8,4))
st.pyplot(fig) # instead of plt.show()


# In[19]:


def main():
    st.title("Real-Time Stock Price Forecasting")
    st.divider()
    get_ticker()
    choose_ticker()
    
if __name__ == "__main__":
    main()

