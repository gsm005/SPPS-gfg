# Stock Price Prediction App using Machine Learning
This is a web app that uses an XGBoost Regressor model to predict the closing stock price of a company, for demonstration purpose we have used Adani Enterprise based on the given input of Open, High, Low, and Volume values.

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

## How it works
The app loads the historical stock data of Adani Enterprise from the "ADANIENT.csv" file and uses it to train an XGBoost Regressor model to predict the closing price of the stock based on the input values of Open, High, Low, and Volume.

The user can input the values for Open, High, Low, and Volume through the number input fields provided on the app. Upon clicking the "Submit" button, the app uses the trained model to predict the closing price for the given input values and displays the result to the user.

## Credits
This app was created by CloudCreators as part of Solve for India Hackathon.

