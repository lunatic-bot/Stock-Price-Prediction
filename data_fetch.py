import yfinance as yf

# Download stock data
data = yf.download('AAPL', start='2014-01-01', end='2024-01-01')

# Save the data to a CSV file
data.to_csv('AAPL_stock_data.csv')