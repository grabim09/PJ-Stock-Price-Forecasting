#!/usr/bin/env python
# coding: utf-8

# In[46]:


import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


# In[47]:


# Read and print the stock tickers that make up S&P500
tickers_data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers_symbol = tickers_data.Symbol.to_list()
tickers_name = tickers_data.Security.to_list()
tuples = [(idx,(sym, name)) for idx, (sym, name) in enumerate(zip(tickers_symbol, tickers_name))]
tickers = dict(tuples)
# print(tickers)


# In[79]:


period_format = {
    "day": {
        "Code": "d",
        "Max Period": 30
    },
    "month": {
        "Code": "m",
        "Max Period": 12
    },
    "year": {
        "Code": "y",
        "Max Period": 10
    }
}
# available_period_format = pd.DataFrame(period_format).T
# available_period_format
# list(period_format.keys())[0]
# period_format["day"]
# period_format.get("day")["Code"]


# In[66]:


available_tickers = pd.DataFrame(tickers).T
available_tickers.columns = ['Symbol', 'Name']
available_tickers['Symbol - Name'] = available_tickers['Symbol'] + ' - ' + available_tickers['Name']
# print(tickers_list)
chosen_ticker_sn = st.selectbox("Please select available ticker below!",available_tickers['Symbol - Name'])
chosen_ticker_symbol = available_tickers.loc[available_tickers['Symbol - Name'] == chosen_ticker_sn, 'Symbol'].item()
chosen_ticker_symbol = "GOOGL"
chosen_period_format = st.selectbox("Select period format",list(period_format.keys()))
final_period_format = period_format.get(chosen_period_format)["Code"]
final_period_value = st.slider("Choose Period", 0, period_format.get(chosen_period_format)["Max period"], 3)
final_period = str(final_period_value) + final_period_format
st.write("Final period is {}".format(final_period))
# st.write("I'm ", age, 'years old')
stock_data = yf.download(tickers = chosen_ticker_symbol, period = "17d", interval = "5m")
stock_data.drop(stock_data.loc[stock_data['Volume'] == 0].index, inplace = True)
# stock_data
row_amount = stock_data.shape[0]
st.write("You have chosen {} Tickers. Acquired {} data points".format(chosen_ticker_sn, row_amount))
st.write("Acquired stock data from {} until {}".format(stock_data.index[0],stock_data.index[row_amount-1]))
st.dataframe(stock_data, height = 200, use_container_width = True)
# print("Acquired stock data from {} until {}".format(stock_data.index[0],stock_data.index[row_amount-1]))


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

