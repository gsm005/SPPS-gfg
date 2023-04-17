# StockMate: A Machine Learning and NLP-Based Stock Price Prediction Webapp

## PROBLEM STATEMENT
Predicting the stock prices is a difficult task as the price of stock is influenced by a variety of factors such as economic indicators, political events ,company-specific news, and investor sentiment which tells  us that we cannot use a machine learning algorithm alone to predict the stock prices as they do not  takes these factors in account.  
To solve this problem, We have proposed a solution for this problem by incorporating Machine learning  and NLP.

For now we have designed a web app that uses an XGBoost Regressor model to predict the closing stock price of a company, for demonstration purpose we have used Adani Enterprise based on the given input of Open, High, Low, and Volume values.


## Note
The webapp is ready for phase 1 of hackathon. We will soon be incorporating more features such as NLP in phase 2.

## Requirements
To run this app, you need the following:

Python 3.6 or later
Streamlit
Requests
Numpy
Matplotlib
Scikit-learn
XGBoost
You can install all these dependencies using pip.

## Methodology
In this project, We have used XG Boost to implement the stock price prediction project.  XG Boost is a popular and powerful machine learning algorithm for stock price prediction because of its ability to handle large datasets, its robustness to noise and its ability to model the non linear relationship between features and target variables. It uses a decision tree based model which can handle non linear relationships between features and target variables. Built in feature selection, built in regularization and can handle large datasets. 

For the NLP part which is in development for phase 2 of the hackathon, we are using LDA algorithm to extract the sentiments floating in the market for a particular company. That will helps us in taking these factors in consideration as economic indicators, political events ,company-specific news, and investor sentiments.

## How it works
The app loads the historical stock data of Adani Enterprise from the "ADANIENT.csv" file and uses it to train an XGBoost Regressor model to predict the closing price of the stock based on the input values of Open, High, Low, and Volume.

The user can input the values for Open, High, Low, and Volume through the number input fields provided on the app. Upon clicking the "Submit" button, the app uses the trained model to predict the closing price for the given input values and displays the result to the user.

## Credits
This app was created by CloudCreators as part of Solve for India Hackathon.

