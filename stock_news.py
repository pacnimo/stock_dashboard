import yfinance as yf
import streamlit as st
from datetime import datetime
import logging

def display_stock_news(ticker):
    logging.basicConfig(level=logging.INFO)
    stock = yf.Ticker(ticker)
    
    try:
        # Retrieve news related to the stock
        stock_news = stock.news

        # Display each news item in the Streamlit app
        for news in stock_news:
            st.subheader(news.get('title', 'No title available'))  # Safely get the news headline
            st.write("Publisher:", news.get('publisher', 'No publisher available'))  # Safely get the news publisher
            st.write("Link:", news.get('link', 'No link available'))  # Provide the link to the full news
            # Attempt to print the publication date; handle UNIX timestamp conversion if present
            date = news.get('providerPublishTime', None)
            if date:
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
            st.write("Date:", date if date else 'No date available')
            st.markdown("-------------------------------------------------------")
    
    except Exception as e:
        st.error("Failed to load stock news: " + str(e))
        logging.error("Error fetching stock news for {}: {}".format(ticker, e))
