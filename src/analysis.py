'''ESta função é a mesma de EDA.ipynb, mas salva os gráficos
     como arquivos HTML para serem usados no front-end.'''

import plotly.graph_objects as go
import pandas as pd
from charts import (candlestick_chart, moving_average_chart, volatility_line,
    volatility_box_by_month, weekly_volume_bar, return_distribution_plot,
    correlation_heatmap, volume_price_scatter, decomp)

DATA_PATH = "../data/dataprocessed/AAPL_data.csv"
OUTPUT_DIR = "../frontend/artifacts/"
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

data = pd.read_csv('../data/dataprocessed/AAPL_data.csv')

def save_plotly_html(fig: go.Figure, path: str):
    fig.write_html(path)

save_plotly_html(
    candlestick_chart(data),
    os.path.join(OUTPUT_DIR, "candlestick_chart.html")
)
save_plotly_html(
    moving_average_chart(data),
    os.path.join(OUTPUT_DIR, "moving_average_chart.html")
)
save_plotly_html(
    volatility_line(data),
    os.path.join(OUTPUT_DIR, "volatility_line.html")
)
save_plotly_html(
    volatility_box_by_month(data),
    os.path.join(OUTPUT_DIR, "volatility_box_by_month.html")
)
save_plotly_html(
    weekly_volume_bar(data),
    os.path.join(OUTPUT_DIR, "weekly_volume_bar.html")
)
save_plotly_html(
    return_distribution_plot(data),
    os.path.join(OUTPUT_DIR, "return_distribution_plot.html")
)
save_plotly_html(
    correlation_heatmap(data),
    os.path.join(OUTPUT_DIR, "correlation_heatmap.html")
)
save_plotly_html(
    volume_price_scatter(data),
    os.path.join(OUTPUT_DIR, "volume_price_scatter.html")
)
save_plotly_html(
    decomp(data),
    os.path.join(OUTPUT_DIR, "decomp.html")
)
print("All analysis charts have been saved to the artifacts directory.")