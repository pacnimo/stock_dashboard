import yfinance as yf
import streamlit as st
from datetime import datetime
import logging
import time
import json

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def display_stock_news(ticker):
    stock = yf.Ticker(ticker)
    
    try:
        # Retrieve news related to the stock
        stock_news = stock.news

        if not stock_news:  # Check if news is empty
            st.warning("No news available for this ticker.")
            logging.info(f"No news data returned for ticker {ticker}.")
            return
        
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

    except ValueError as e:
        st.error(f"Failed to load stock news due to a value error: {e}")
        logging.error(f"Value error fetching stock news for {ticker}: {e}")
    except Exception as e:
        st.error(f"Failed to load stock news: {e}")
        logging.error(f"Unexpected error fetching stock news for {ticker}: {e}")

