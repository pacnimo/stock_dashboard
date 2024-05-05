import yfinance as yf
import streamlit as st

def display_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    # Create a formatted string to display as a paragraph
    company_info = f"""
    **Sector**: {info.get('sector', 'N/A')}\n
    **Full Time Employees**: {info.get('fullTimeEmployees', 'N/A')}\n
    **Business Summary**: {info.get('longBusinessSummary', 'N/A')}
    """
    st.markdown(company_info)

