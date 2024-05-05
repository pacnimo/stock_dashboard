import yfinance as yf
import plotly.express as px
import streamlit as st

def display_earnings_chart(ticker):
    stock = yf.Ticker(ticker)
    # Get financials data, ensuring it includes data from the last 5 years
    financials = stock.financials
    # Extracting Net Income
    if "Net Income" in financials.index:
        net_income = financials.loc["Net Income"]
        # Ensure we are capturing the last 5 years of data
        if len(net_income) >= 5:
            net_income = net_income.iloc[:5]  # Get only the last 5 entries
        years = net_income.index.strftime('%Y')
        fig = px.bar(x=years, y=net_income.values, labels={'x': 'Year', 'y': 'Net Income'}, title="Annual Net Income")
        st.plotly_chart(fig)
    else:
        st.error("Net Income data not available.")

