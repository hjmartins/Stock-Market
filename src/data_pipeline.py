import os 
import pandas as pd
import numpy as np
from datetime import datetime
import logging  
import yfinance as yf
DATA_DIR = os.path.join(os.path.dirname(__file__),'../data/dataprocessed/')
os.makedirs(DATA_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def search_stock(ticker: str, period: str = '1y', interval: str = '1d') -> pd.DataFrame:
    try:
        df =yf.download(ticker, period=period, interval=interval)
        df.reset_index(inplace=True)
        df.dropna(inplace=True)
        return df
    except Exception as e:
        logging.error(f"Error fetching data for ticker {ticker}: {e}")
        return pd.DataFrame()

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        logging.warning("Empty DataFrame provided to clean_data.")
        return df
    '''
Date

('Close', 'AAPL')

('High', 'AAPL')

('Low', 'AAPL')

('Open', 'AAPL')

('Volume', 'AAPL')
    df.columns = [col[0] if col[1] == '' else col[1] for col in df.columns]
    '''
    df = df.rename(columns={
        'Open': 'open',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Adj Close': 'adj_close',
        'Volume': 'volume'
    })
    df = df[df['Date'].notna()]

    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)

    df = df[~df.index.duplicated()].dropna()

    return df

def save_data(df: pd.DataFrame, ticker: str) -> None:
    if df.empty:
        logging.warning("Empty DataFrame provided to save_data.")
        return
    filepath = os.path.join(DATA_DIR, f"{ticker}_data.csv")
    df.to_csv(filepath, index=False)
    logging.info(f"Data saved to {filepath}")

def pipeline_load(ticker: str, period: str = '1y', interval: str = '1d') -> pd.DataFrame:
    raw = search_stock(ticker, period, interval)
    processed = clean_data(raw)
    save_data(processed, ticker)
    logging.info(f"Pipeline completed for ticker {ticker}")
    return processed
if __name__ == "__main__":
    df = pipeline_load('AAPL', '1y', '1d')
    print(df.head())