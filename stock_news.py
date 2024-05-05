import yfinance as yf
import streamlit as st

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
