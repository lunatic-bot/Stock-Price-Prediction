# Stock Price Prediction using LSTM

This repository contains code for predicting stock prices using various time series models, starting with Long Short-Term Memory (LSTM) neural networks. The initial implementation predicts future stock prices based on historical data obtained from Yahoo Finance using the `yfinance` library.

## Table of Contents

- [Overview](#overview)
- [Data Collection](#data-collection)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling with LSTM](#modeling-with-lstm)
- [Future Work](#future-work)
- [How to Run the Code](#how-to-run-the-code)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Overview

In this project, I have implemented a stock price prediction model using LSTM, a type of recurrent neural network (RNN) designed to capture long-term dependencies in time series data. The dataset consists of historical stock prices fetched from Yahoo Finance, and I used various techniques to explore and analyze the data before building the prediction model.

## Data Collection

The stock market data is collected using the `yfinance` library, which allows easy access to Yahoo Finance's historical stock data. In this case, I have used the stock data for **Apple Inc. (AAPL)**, but you can modify the ticker symbol to collect data for other stocks.

## Exploratory Data Analysis (EDA)

Exploratory data analysis was performed using `pandas` and `matplotlib`. In this phase, I visualized trends, calculated daily returns, and analyzed volatility.

Some of the key analyses include:

- Plotting closing prices over time
- Calculating daily returns
- Computing volatility based on stock price movements

## Modeling with LSTM

The core of this project is building a stock price prediction model using LSTM, a deep learning model suitable for time series forecasting. The LSTM model was built using Keras and TensorFlow, and trained on scaled stock price data.

Key steps in the modeling process:

1. Data Preprocessing: Scaling the stock price data to fit into a range between 0 and 1 using MinMaxScaler.
2. LSTM Model: The LSTM model is constructed with two LSTM layers and dense layers for output predictions.
3. Training: The model is trained using historical stock prices, predicting future prices based on a sequence of past stock data.

## Future Work

In addition to the LSTM model, I plan to implement and compare other time series forecasting models, including:

- ARIMA (AutoRegressive Integrated Moving Average)
- SARIMA (Seasonal ARIMA)
- Prophet
- RNN Variants
  The goal is to evaluate which model performs best in predicting stock prices.

## How to Run the Code

1. Clone this repository to your local machine

   ```bash
   git clone https://github.com/lunatic-bot/Stock-Price-Prediction.git
   cd Stock-Price-Prediction

   ```

2. Install the required dependencies
3. Run the Stock_Price_Prediction.ipynb Jupyter notebook.

## Installation

To install the necessary libraries and dependencies, create a virtual environment and use the requirements.txt file.

    ```bash
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate   # For Windows: venv\Scripts\activate

    # Install the dependencies
    pip install -r requirements.txt
