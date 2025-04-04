# data_loader.py
import yfinance as yf
import pandas as pd

def download_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == '__main__':
    # Download historical data for S&P 500 and VIX
    sp500 = download_data("^GSPC", "2000-01-01", "2024-01-01")
    vix = download_data("^VIX", "2000-01-01", "2024-01-01")
    
    # Save data to CSV files for later use
    sp500.to_csv("sp500.csv")
    vix.to_csv("vix.csv")
    
    print("Data downloaded and saved as sp500.csv and vix.csv")
