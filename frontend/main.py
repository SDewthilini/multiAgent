import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import yfinance as yf

# Initialize the Streamlit app
st.set_page_config(page_title="AI Stock Investment Chat", layout="wide")

st.title("💬 AI-Powered Stock Investment Advisor")

# Sidebar info
st.sidebar.info("This chatbot analyzes stock market data and suggests the top 5 investible stocks.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Function to get stock data from Yahoo Finance
def get_stock_data(ticker):
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=30)
    stock = yf.download(ticker, start=start_date, end=end_date)
    return stock


# Simulated AI function to get top 5 investible stocks (Replace with actual multi-agent system)
def get_top_stocks():
    return ["AAPL", "TSLA", "MSFT", "GOOGL", "NVDA"]


# Chat UI
with st.chat_message("assistant"):
    st.write("Ask me about stock investments!")

user_input = st.chat_input("Ask me: What are the top stocks to invest in?")

if user_input:
    # Store user query
    st.session_state.messages.append({"role": "user", "content": user_input})

    # AI Response: Get top 5 investible stocks
    top_stocks = get_top_stocks()
    response_text = f"Based on my analysis, the top 5 investible stocks are: {', '.join(top_stocks)}"

    # Display AI response
    with st.chat_message("assistant"):
        st.write(response_text)

    # Store response
    st.session_state.messages.append({"role": "assistant", "content": response_text})

    # Plot stock price trends for the last month
    st.subheader("📈 Stock Price Trends (Last Month)")
    for stock in top_stocks:
        st.write(f"*{stock} - Stock Price Trend*")
        stock_data = get_stock_data(stock)

        if not stock_data.empty:
            st.line_chart(stock_data["Close"])  # Plot closing price over time
        else:
            st.warning(f"Could not fetch data for {stock}.")