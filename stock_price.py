import yfinance as yf
import plotly.express as px
import streamlit as st
import time

def display_stock_price_chart(ticker="AAPL"):
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
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
            break  # If successful, break the loop

        except Exception as e:
            attempts += 1
            st.error(f"Attempt {attempts}: Failed to download or display stock price data for {ticker}: {e}")
            time.sleep(1)  # Sleep for a bit before retrying

    if attempts == max_attempts:
        st.error("Failed to display data after several attempts. Please check your network connection and try again later.")
