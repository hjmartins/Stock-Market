import streamlit as st
import pandas as pd
import os  
from pathlib import Path
import streamlit.components.v1 as components
import src.charts as ch 
st.set_page_config(
    page_title="Stock Market Analysis",
    layout="wide")
st.title('Stock Market Analysis Dashboard')#1
st.plotly_chart(ch.plot_close_price(), use_container_width=True)
st.markdown("## Candlestick Chart")#2
st.plotly_chart(ch.candlestick_chart(), use_container_width=True)
st.markdown("## Volatility Over Time")#3  
st.plotly_chart(ch.volatility(), use_container_width=True)  
st.markdown("## Average Monthly Return")#4
st.plotly_chart(ch.average_monthly_return(), use_container_width=True)
st.markdown("## Moving Averages")#5
st.plotly_chart(ch.moving_averages(), use_container_width=True)
st.markdown("## Weekly Volume Bar Chart")#6
st.plotly_chart(ch.average_return_by_day_of_week(), use_container_width=True)
st.markdown("## Correlation between Volume and Volatility")#7
st.plotly_chart(ch.correlation_volume_volatility(), use_container_width=True)
#st.markdown("## Seasonal Decomposition")#8
#st.plotly_chart(ch.decomp(), use_container_width=True)
st.markdown("## Additional Analysis Charts")
