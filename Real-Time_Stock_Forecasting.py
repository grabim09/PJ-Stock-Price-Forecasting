#!/usr/bin/env python
# coding: utf-8

# In[15]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


# In[24]:


# Read and print the stock tickers that make up S&P500
tickers_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers_symbol = tickers_data.Symbol.to_list()
tickers_name = tickers_data.Security.to_list()
tuples = [(idx,(sym, name)) for idx, (sym, name) in enumerate(zip(tickers_symbol, tickers_name))]
tickers = dict(tuples)
# print(tickers)


# In[25]:


tickers_list = pd.DataFrame(tickers).T
tickers_list.columns = ['Symbol', 'Name']
tickers_list['Symbol - Name'] = tickers_list['Symbol'] + ' - ' + tickers_list['Name']
# print(tickers_list)


# In[37]:


chosen_ticker_sn = st.selectbox("Please select available ticker below!",tickers_list['Symbol - Name'])
chosen_ticker_symbol = tickers_list.loc[tickers_list['Symbol - Name'] == chosen_ticker_sn, 'Symbol'].item()
# chosen_ticker_symbol = "GOOGL"
stock_data = yf.download(tickers = chosen_ticker_symbol, period = "7d", interval = "5m")
stock_data.drop(stock_data.loc[stock_data['Volume'] == 0].index, inplace = True)
# stock_data
st.write("You have chosen {} Tickers. Acquired {} data points".format(choosen_ticker_sn, stock_data.shape[0]))
st.dataframe(stock_data, height = 200, use_container_width = True)


# In[18]:


stock_data['Adj Close'].plot()
plt.show()
fig = plt.figure(figsize=(8,4))
st.pyplot(fig) # instead of plt.show()


# In[19]:


# def main():
#     st.title("Real-Time Stock Price Forecasting")
#     st.divider()
#     get_ticker()
    
# if __name__ == "__main__":
#     main()

