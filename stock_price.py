import yfinance as yf
import plotly.express as px
import streamlit as st

def display_stock_price_chart(ticker):
    data = yf.download(ticker, period="5y")
    fig = px.line(data, x=data.index, y="Close", title=f"Closing Prices for {ticker}")
    st.plotly_chart(fig)
