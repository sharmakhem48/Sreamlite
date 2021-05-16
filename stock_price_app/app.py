import streamlit as st
import yfinance as yf
import datetime
import webbrowser
import requests
from footer_utils import footer


def onclick(url):
    webbrowser.open(url)
    
    
heading  = """
         This is stock price app
         """
st.header(heading)

col1, col2, col3 = st.beta_columns(3)
with col1:
    ticker_symbol = st.text_input('Enter your ticker value....', value='AAPL', help='ex..AAPL,GOOGL')
    
with col2:
    start = st.date_input('Enter start date', value =datetime.datetime(2010,1,1), min_value=datetime.datetime(2010,1,1))
    
    
with col3:
    end = st.date_input('Enter end date', value =datetime.datetime(2020,1,1), min_value=datetime.datetime(2020,1,1))
    

st.sidebar.header('Menu')
button1 = st.sidebar.button('About Developer')
button2 = st.sidebar.button('About Streamlite')

if button1:
    onclick('https://sharmakhem48.github.io')
    
if button2:
    onclick('https://streamlit.io/')


data = yf.Ticker(ticker_symbol)

ticker_data = data.history(period='1d', start=start, end=end)

st.line_chart(ticker_data.Close)
st.line_chart(ticker_data.Volume)
footer()
