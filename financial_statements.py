# financial_statements.py

import yfinance as yf
import pandas as pd
import streamlit as st

def display_financial_statements(ticker):
    stock = yf.Ticker(ticker)
    
    # Fetch financial statements
    income_statement = stock.income_stmt
    balance_sheet = stock.balance_sheet
    cash_flow_statement = stock.cashflow
    
    # Display financial statements
    st.sidebar.subheader("Income Statement")
    if not income_statement.empty:
        st.sidebar.write(income_statement)
    else:
        st.sidebar.write("No income statement data available.")

    st.sidebar.subheader("Balance Sheet")
    if not balance_sheet.empty:
        st.sidebar.write(balance_sheet)
    else:
        st.sidebar.write("No balance sheet data available.")

    st.sidebar.subheader("Cash Flow Statement")
    if not cash_flow_statement.empty:
        st.sidebar.write(cash_flow_statement)
    else:
        st.sidebar.write("No cash flow statement data available.")

