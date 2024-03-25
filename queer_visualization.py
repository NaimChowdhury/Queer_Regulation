import pandas as pandas

import plotly.graph_objects as go

# Data
events = ['罪化与病态化的中国', '非罪化与半去病化的中国', '中国新时代的监管']
start_years = [1958, 2002, 2015]
end years = [2001, 2014, 2024]

# Calculate duration of each event
durations = [end - start for start, end in zip(start_years, end_years)]

# Instantiate a plotly figure
fig = go.Figure()