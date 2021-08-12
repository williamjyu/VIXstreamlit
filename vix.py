import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import date

# heading
st.title('Cboe Volatility Index (VIX) on Historical Moments')
st.subheader('By William Yu')

# description
st.markdown('####')
st.write('''
[VIX is the ticker symbol and the popular name for the Chicago Board Options Exchange's CBOE Volatility Index, 
a popular measure of the stock market's expectation of volatility based on S&P 500 index options. 
It is calculated and disseminated on a real-time basis by the CBOE, and is often referred to as the fear index or fear gauge.]
(https://www.google.com/finance/quote/VIX:INDEXCBOE?sa=X&ved=2ahUKEwjb8qLSxafyAhUHuZ4KHcd7BoEQ_AUoAXoECAEQAw)
''')

# yfinance data collection
vix = '^VIX'
ticker_data = yf.Ticker(vix)

# function for putting chart on streamlit
start = None
end = None


def make_chart(date1, date2):
    ticker_df = ticker_data.history(period='1d', start=date1, end=date2)
    st.line_chart(ticker_df.Close)


box1 = False
box2 = False
box3 = False
box4 = False
box5 = False
box6 = False
box7 = False
box8 = False
box9 = False
box10 = False
box11 = False
box12 = False

# first row 
st.markdown('#####')
st.subheader('Examine the volatility around famous historical moments:')
st.markdown('####')
c1, c2, c3, c4 = st.beta_columns(4)

with c1:
    if st.checkbox('Early 1990s Recession'):
        box1 = True

with c2:
    if st.checkbox('Asian Financial Crisis'):
        box2 = True

with c3:
    if st.checkbox('Dot-com Bubble'):
        box3 = True

with c4:
    if st.checkbox('Chinese Stock Market Bubble'):
        box4 = True

# second row
c5, c6, c7, c8 = st.beta_columns(4)

with c5:
    if st.checkbox('2008 Financial Crisis'):
        box5 = True

with c6:
    if st.checkbox('European Debt Crisis'):
        box6 = True

with c7:
    if st.checkbox('2010 Flash Crash'):
        box7 = True

with c8:
    if st.checkbox('2011 Debt Ceiling Crisis'):
        box8 = True

# third row
c9, c10, c11, c12 = st.beta_columns(4)

with c9:
    if st.checkbox('2015-2016 Selloff'):
        box9 = True

with c10:
    if st.checkbox('US-China Trade War'):
        box10 = True

with c11:
    if st.checkbox('2020 US Election'):
        box11 = True

with c12:
    if st.checkbox('COVID-19'):
        box12 = True

# plotting charts on streamlit
if box1:
    st.subheader('Early 1990s Recession')
    make_chart('1990-2-1', '1993-7-1')

if box2:
    st.subheader('Asian Financial Crisis')
    make_chart('1996-12-1', '1998-5-1')

if box3:
    st.subheader('Dot-com Bubble')
    make_chart('1998-5-1', '2002-10-9')

if box4:
    st.subheader('Chinese Stock Market Bubble')
    make_chart('2007-1-1', '2008-5-1')

if box5:
    st.subheader('2008 Financial Crisis')
    make_chart('2007-1-1', '2010-3-1')

if box6:
    st.subheader('European Debt Crisis')
    make_chart('2010-3-1', '2012-3-1')

if box7:
    st.subheader('2010 Flash Crash')
    make_chart('2010-5-1', '2010-5-15')

if box8:
    st.subheader('2011 Debt Ceiling Crisis')
    make_chart('2011-5-1', '2011-10-1')

if box9:
    st.subheader('2015-2016 Selloff')
    make_chart('2015-4-1', '2016-7-1')

if box10:
    st.subheader('US-China Trade War')
    make_chart('2017-12-1', '2019-12-1')

if box11:
    st.subheader('2020 US Election')
    make_chart('2020-10-1', '2020-11-10')

if box12:
    st.subheader('COVID-19')
    make_chart('2020-1-15', '2020-5-1')

st.markdown('#')

# enter your own timeframe
if st.checkbox('Enter your own timeframe'):
    user_start = st.date_input('Start date')
    user_end = st.date_input('End date')

    st.subheader(f'VIX from {user_start} to {user_end}')
    make_chart(user_start, user_end)

# SPY, QQQ, and DIA with VIX
st.markdown('##')
st.subheader('Compare VIX to S&P 500, NASDAQ, and Dow Jones')

box13 = False
box14 = False
box15 = False

st.markdown('#####')
c13, c14, c15 = st.beta_columns(3)

with c13:
    if st.checkbox('S&P 500'):
        box13 = True

with c14:
    if st.checkbox('NASDAQ'):
        box14 = True

with c15:
    if st.checkbox('Dow Jones'):
        box15 = True


sp = 'SPY'
qqq = 'QQQ'
dia = 'DIA'

today = date.today()

# sorting data and plotting on streamlit
if box13:
    spdata = yf.Ticker(sp)

    sp_df = spdata.history(period='1d', start='1993-2-1', end=today)
    ticker_df = ticker_data.history(period='1d', start='1993-2-1', end=today)

    sp_df = sp_df.rename(columns={'Close':'SPY Close'})
    ticker_df = ticker_df.rename(columns={'Close':'VIX Close'})

    sp_comp_df = pd.concat([ticker_df['VIX Close'], sp_df['SPY Close']], axis=1)

    st.subheader('$SPY and ^VIX')
    st.line_chart(sp_comp_df)

if box14:
    qqqdata = yf.Ticker(qqq)

    qqq_df = qqqdata.history(period='1d', start='1999-4-1', end=today)
    ticker_df = ticker_data.history(period='1d', start='1999-4-1', end=today)

    qqq_df = qqq_df.rename(columns={'Close':'QQQ Close'})
    ticker_df = ticker_df.rename(columns={'Close':'VIX Close'})

    qqq_comp_df = pd.concat([ticker_df['VIX Close'], qqq_df['QQQ Close']], axis=1)

    st.subheader('$QQQ and ^VIX')
    st.line_chart(qqq_comp_df)

if box15:
    diadata = yf.Ticker(dia)

    dia_df = diadata.history(period='1d', start='1998-2-1', end=today)
    ticker_df = ticker_data.history(period='1d', start='1998-2-1', end=today)

    dia_df = dia_df.rename(columns={'Close':'DIA Close'})
    ticker_df = ticker_df.rename(columns={'Close':'VIX Close'})

    dia_comp_df = pd.concat([ticker_df['VIX Close'], dia_df['DIA Close']], axis=1)

    st.subheader('$DIA and ^VIX')
    st.line_chart(dia_comp_df)

# footer
st.markdown('#')
st.write('''
*Data sourced from [Yahoo Finance](https://finance.yahoo.com/quote/%5EVIX?p=^VIX&.tsrc=fin-srch)*
''')
