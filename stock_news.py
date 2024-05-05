import yfinance as yf
import streamlit as st

def display_stock_news(ticker):
    stock = yf.Ticker(ticker)
    try:
        stock_news = stock.news
        if not stock_news:  # Check if news list is empty
            st.warning('No news items found.')
            return
    except Exception as e:
        st.error("An error occurred while fetching the news.")
        st.text(f"Error details: {str(e)}")
        return

    for news in stock_news:
        st.subheader(news.get('title', 'No title available'))
        st.write("Publisher:", news.get('publisher', 'No publisher available'))
        st.write("Link:", news.get('link', 'No link available'))
        date = news.get('providerPublishTime')
        if date:
            from datetime import datetime
            date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
        st.write("Date:", date if date else 'No date available')
        st.markdown("-------------------------------------------------------")
