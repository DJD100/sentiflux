import streamlit as st

st.set_page_config(page_title="Sentiflux", layout="wide")

st.title("📊 Sentiflux – AI-Powered Stock Sentiment Dashboard")

st.markdown("Welcome to **Sentiflux**. Here's a look at some trending tickers and their sentiment analysis.")

# Simulated trending tickers and sentiment data
tickers = {
    "AAPL": {"sentiment": "Positive", "summary": "Strong earnings report, increased demand for iPhones."},
    "TSLA": {"sentiment": "Negative", "summary": "Production delays and recent controversy causing concerns."},
    "NVDA": {"sentiment": "Positive", "summary": "Surging AI chip demand; strong future outlook."},
    "AMZN": {"sentiment": "Neutral", "summary": "Mixed earnings report; stable revenue, rising costs."},
    "MSFT": {"sentiment": "Positive", "summary": "Cloud growth and enterprise expansion continue to lead."}
}

for ticker, data in tickers.items():
    st.subheader(f"{ticker} – Sentiment: {data['sentiment']}")
    st.write(f"**Summary:** {data['summary']}")
    st.markdown("---")
