import pandas as pd
a300=pd.read_csv('/tmp/A300.csv', index_col='date', parse_dates=True)
avgA_baostock=pd.read_csv('/tmp/avgA_baostock.csv', index_col='date', parse_dates=True)


# 累积收益率
import plotly_express as px
px.line(a300.cumsum().reset_index(), x = 'date', y='log_ret')

px.line(avgA_baostock.cumsum().reset_index(), x = 'date', y='return')


# 频率图
px.histogram(a300, x="log_ret")

px.histogram(avgA_baostock, x="return")
