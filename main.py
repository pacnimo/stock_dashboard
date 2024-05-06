import streamlit as st
import yfinance as yf
import plotly.express as px

# Set page configuration with page title, layout, and initial sidebar state
st.set_page_config(
    page_title="Free Stock Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Free Stock Analytics Dashboard..."
    }
)

st.title('Free Stock Analytics Dashboard')

# Display Stock News
def display_stock_news(ticker="AAPL"):
    # Fetch the data for the given stock ticker
    stock = yf.Ticker(ticker)

    try:
        # Retrieve news related to the stock
        stock_news = stock.news

        # Check if the news list is empty
        if not stock_news:
            st.warning("No news available for this ticker.")
            return

        # Display each news item in the Streamlit app
        for news in stock_news:
            st.subheader(news.get('title', 'No title available'))  # Safely get the news headline
            st.write("Publisher:", news.get('publisher', 'No publisher available'))  # Safely get the news publisher
            st.write("Link:", news.get('link', 'No link available'))  # Provide the link to the full news
            date = news.get('providerPublishTime', None)
            if date:
                from datetime import datetime
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
            st.write("Date:", date if date else 'No date available')
            st.markdown("-------------------------------------------------------")
    except Exception as e:
        st.error(f"Failed to load stock news: {e}")

# Display Company Information
def display_company_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    
    # Extract the longBusinessSummary from the info dictionary
    long_business_summary = info.get('longBusinessSummary', 'No information available')
    
    # Display the longBusinessSummary
    st.write(long_business_summary)


# Display Earnings Chart (Integrated from provided code)
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

# Display Stock Price Chart
def display_stock_price_chart(ticker):
    try:
        data = yf.download(ticker, period="5y")
        if data.empty:
            st.warning("No data available for the selected ticker.")
            return
        fig = px.line(data, x=data.index, y="Close", title=f"Closing Prices for {ticker}")
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Failed to retrieve data for {ticker}. Error: {e}")

# Display Financial Statements in the sidebar
def display_financial_statements_in_sidebar(ticker):
    stock = yf.Ticker(ticker)
    
    # Fetch financial statements
    income_statement = stock.financials
    balance_sheet = stock.balance_sheet
    cash_flow_statement = stock.cash_flow

    # Income Statement
    st.sidebar.subheader("Income Statement")
    if not income_statement.empty:
        st.sidebar.write(income_statement)
    else:
        st.sidebar.write("No income statement data available.")

    # Balance Sheet
    st.sidebar.subheader("Balance Sheet")
    if not balance_sheet.empty:
        st.sidebar.write(balance_sheet)
    else:
        st.sidebar.write("No balance sheet data available.")

    # Cash Flow Statement
    st.sidebar.subheader("Cash Flow Statement")
    if not cash_flow_statement.empty:
        st.sidebar.write(cash_flow_statement)
    else:
        st.sidebar.write("No cash flow statement data available.")

# Display Stock News in the sidebar
def display_stock_news_in_sidebar(ticker):
    st.sidebar.subheader(f"Latest News for {ticker}")
    display_stock_news(ticker)

# Input for Stock Ticker
ticker = st.sidebar.text_input('Enter Stock Ticker', 'AAPL')

# Display Financial Statements in the sidebar for the entered ticker
display_financial_statements_in_sidebar(ticker)

# Define the two columns for the first row
col1, col2 = st.columns(2)

with col1:
    st.header(f"{ticker} Company Info")
    display_company_info(ticker)

with col2:
    st.header(f"{ticker} Earnings Last 5 Years")
    display_earnings_chart(ticker)

# Define the second row for the stock price chart
col4, col3 = st.columns(2)

with col3:
    st.header(f"{ticker} Price Graph (5 Years)")
    display_stock_price_chart(ticker)

with col4:
    # Display Stock News in the sidebar for the entered ticker
    display_stock_news_in_sidebar(ticker)

# Add footer with GitHub repo link and license information
st.markdown("""
---
**GitHub Repository:** [Link to GitHub](https://github.com/pacnimo/stock_dashboard)

**License:** Apache 2.0

_Free Stock Analytics Dashboard is not responsible for any trading losses incurred by users of this application._
""")
