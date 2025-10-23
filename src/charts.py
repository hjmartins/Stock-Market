import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
import os
#1
def plot_close_price():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)   
    fig = px.line(data, x='Date', y='close',
                 title='Close Price Over Time',
                   template='plotly_dark')
    fig.update_xaxes(rangeslider_visible=True)
    return fig
def candlestick_chart():#2
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['open'],
                                         high=data['high'],
                                         low=data['low'],
                                         close=data['close'])])
    fig.update_layout(title='Candlestick Chart',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      template='plotly_dark',
                      xaxis_rangeslider_visible=True)
    return fig

def volatility():#3
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')
    data['return'] = data['close'].pct_change(fill_method='pad')
    data['volatility'] = data['return'].rolling(window=20).std()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['volatility'],
                             mode='lines',
                             name='20-Day Rolling Volatility',
                             line=dict(color='orange')))
    fig.update_layout(title='Stock Volatility Over Time',
                      xaxis_title='Date',yaxis_title='Volatility',
                      template='plotly_dark')
    return fig
def average_monthly_return():#4
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')
    data['return'] = data['close'].pct_change(fill_method='pad')
    data['Month'] = data['Date'].dt.month_name()
    monthly_returns = data.groupby('Month')['return'].mean().reindex([
        'January','February','March','April','May','June',
        'July','August','September','October','November','December'
    ])

    fig = go.Figure(go.Bar(
        x=monthly_returns.index, y=monthly_returns.values,
        marker_color='lightskyblue'
    ))
    fig.update_layout(
        title=' Average Monthly Returns',
        xaxis_title='Month', yaxis_title='Average Return',
        template='plotly_dark'
    )
    return fig
def average_return_by_day_of_week():#5
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')
    data['return'] = data['close'].pct_change(fill_method='pad')
    data['DayOfWeek'] = data['Date'].dt.day_name()
    daily_returns = data.groupby('DayOfWeek')['return'].mean().reindex([
        'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'
    ])

    fig = go.Figure(go.Bar(
        x=daily_returns.index, y=daily_returns.values,
        marker_color='mediumturquoise'
    ))
    fig.update_layout(
        title=' Average Return by Day of Week',
        xaxis_title='Day of Week', yaxis_title='Average Return',
        template='plotly_dark'
    )
    return fig

def correlation_volume_volatility():#6
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')
    #data['return'] = data['close'].pct_change(fill_method='pad')
    data['Volatility'] = data['close'].pct_change().rolling(window=20).std()
    data['volume'] = pd.to_numeric(data['volume'], errors='coerce')
    data['Volatility'] = pd.to_numeric(data['Volatility'], errors='coerce')


    data['roll_corr'] = data['volume'].rolling(window=20).corr(data['Volatility'])


    fig = px.line(data.dropna(subset=['roll_corr']), x='Date', y='roll_corr',
              title='Correlação Móvel entre Volume e Volatilidade (20 dias)',
              template='plotly_dark')
    return fig
def moving_averages():#7
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)

    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')
    #data['return'] = data['close'].pct_change(fill_method='pad')

    data['mm50'] = data['close'].rolling(window=50).mean()
    data['mm20'] = data['close'].rolling(window=20).mean()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['close'], name='Close Price', line=dict(color='royalblue')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['mm50'], name='MA50', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['mm20'], name='MA20', line=dict(color='green')))
    fig.update_layout(title='AAPL Close Price with Moving Averages',template='plotly_white')
    return fig

def decomp():#8
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_path = os.path.join(base_dir, 'data', 'dataprocessed', 'AAPL_data.csv')
    data = pd.read_csv(data_path)
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['Date']= pd.to_datetime(data['Date'])
    data= data.sort_values('Date')

    data_decomp = data.set_index('Date').dropna(subset=['close'])
    decomp = seasonal_decompose(data_decomp['close'], model='additive', period=30)

    fig, axes = plt.subplots(4, 1, figsize=(12,10), sharex=True)
    decomp.observed.plot(ax=axes[0], title='close')
    decomp.trend.plot(ax=axes[1], title='Tendencia')
    decomp.seasonal.plot(ax=axes[2], title='Sazonalidade')
    decomp.resid.plot(ax=axes[3], title='Resíduos')
    plt.tight_layout()
    return plt