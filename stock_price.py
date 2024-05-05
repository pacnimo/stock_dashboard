import yfinance as yf
import plotly.express as px
import streamlit as st

def display_stock_price_chart(ticker="AAPL"):
    try:
        # Download the stock data for the specified ticker over the past 5 years
        data = yf.download(ticker, period="5y")
        
        # Check if the downloaded data is empty
        if data.empty:
            st.warning(f"No price data available for {ticker}.")
            return

        # Create a line chart using Plotly Express
        fig = px.line(data, x=data.index, y="Close", title=f"Closing Prices for {ticker}")
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"Failed to download or display stock price data for {ticker}: {e}")
