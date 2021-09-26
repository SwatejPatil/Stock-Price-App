import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App
Shown are the stock closing price and volume of Zoom!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#define the ticker symbol
tickerSymbol = 'ZM'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1m', start='2018-5-31', end='2021-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write(
    """
    ### Closing Price
    """
)
st.line_chart(tickerDf.Close)

st.write(
    """
    ### Volume Price
    """
)
st.line_chart(tickerDf.Volume)