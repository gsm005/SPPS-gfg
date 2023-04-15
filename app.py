import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import yfinance as yf
from datetime import datetime

tickerSymbol = 'ADANIENT.NS'
stockData = yf.Ticker(tickerSymbol)
today = datetime.today().strftime('%Y-%m-%d')
todayData = stockData.history(start=today)
st.set_page_config(page_title="Stocks",page_icon=":tada:",layout="wide")
model=XGBRegressor() 

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_rMIWDc0fSB.json")

def predict(Open,High,Low,Volume):
    ndf=pd.read_csv('teslanew.csv')
    ndf = pd.concat([ndf, pd.DataFrame({'Open': [Open], 'High': [High], 'Low': [Low], 'Volume': [Volume]})], ignore_index=True)
    x_new=ndf[['Open','High','Low','Volume']]
    y_new_predict=model.predict(x_new)
    return y_new_predict
def main():
        df=pd.read_csv("ADANIENT.csv")
        x=df.drop(['Close','Date','Adj Close'],axis=1)
        y=df['Close']

        model.fit(x, y)
        with st.container():
            l_col,r_col=st.columns(2)
            with l_col:
                st.subheader("Hi,This is Stock Price Predicton System")
                st.title("Adani Enterprise Share Price Predictor")
                st.write("This model is trained using XGBoost Regressor model. This site is for educational purpose.Invest with your own risks.")
                Open = (float)(todayData['Open'].iloc[-1])
                High = (float)(todayData['High'].iloc[-1])
                Low = (float)(todayData['Low'].iloc[-1])
                Volume = (float)(todayData['Volume'].iloc[-1])
                st.write("Open= ",Open)
                st.write("High= ",High)
                st.write("Low= ",Low)
                st.write("Volume= ",Volume)
                
            with r_col:
                st_lottie(lottie_coding,height=300,key='coding')
                result=predict(Open,High,Low,Volume)
                st.write("The predicted close price of the stock is:", result)
main()
