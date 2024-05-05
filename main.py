# main.py
import streamlit as st
from company_info import display_company_info
from earnings import display_earnings_chart
from stock_price import display_stock_price_chart
from financial_statements import display_financial_statements
from stock_news import display_stock_news  # Importing the new function

# Set page configuration with page title, layout and initial sidebar state
st.set_page_config(
    page_title="Free Stock Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/report',
        'About': "Free Stock Analytics Dashboard is a web application for visualizing stock data including company information, financial statements, earnings, and stock price movements. Built with Streamlit, it utilizes data from Yahoo Finance API."
    }
)

st.title('Free Stock Analytics Dashboard')

ticker = st.sidebar.text_input('Enter Stock Ticker', 'AAPL')

# Display "Financial Statements" in the sidebar
st.sidebar.header(f"{ticker} Financial Statements")
display_financial_statements(ticker)

# Define the two columns for the first row
col1, col2 = st.columns(2)

with col1:
    st.header(f"{ticker} Company Info")
    display_company_info(ticker)

with col2:
    st.header(f"{ticker} Earnings Last 5 Years")
    display_earnings_chart(ticker)

# Define the second row
col4 = st.columns(2)


with col4:
    # Display "Price Graph (5 Years)" in the main section
    st.header(f"{ticker} Price Graph (5 Years)")
    display_stock_price_chart(ticker)

# Add footer with GitHub repo link and license information
st.markdown("""
---
**GitHub Repository:** [Link to GitHub](https://github.com/pacnimo/stock_dashboard)

**License:** Apache 2.0

_Free Stock Analytics Dashboard is not responsible for any trading losses incurred by users of this application._
""")

