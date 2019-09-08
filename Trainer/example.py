import tkinter
import pandas as pd
#from pandas.compat import StringIO
#import MySQLdb
import mysql.connector
import sys
import matplotlib.pyplot as plt
import matplotlib

from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

cnx = mysql.connector.connect(user='root', password='tibbtp24',
                              host='127.0.0.1',
                              database='simulator')
cursor = cnx.cursor()
matplotlib.use('TkAgg')
def plot_candlestick(df, ax=None, fmt="%Y-%m-%d"):
    if ax is None:
        fig, ax = plt.subplots(2, figsize=(16, 8), gridspec_kw={'height_ratios': [4, 1]})

    idx_name = df.index.name
    short_rolling = df.rolling(window=20).mean()
    long_rolling = df.rolling(window=200).mean()
    volume_rolling = df.rolling(window=3).mean()
    dat = df.reset_index()[[idx_name, "open", "high", "low", "close"]]
    dat[df.index.name] = dat[df.index.name].map(mdates.date2num)
    ax[0].xaxis_date()
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    plt.xticks(rotation=45)
    _ = candlestick_ohlc(ax[0], dat.values, width=.6, colorup='g', alpha=1)
    ax[0].set_xlabel(idx_name)
    ax[0].set_ylabel("OHLC")
    ax[0].plot(short_rolling['close'])
    ax[0].plot(long_rolling['close'])
    ax[1].plot(volume_rolling['volume'])

    return ax


df = pd.read_sql(
    ('select quotedate,open,high,low,close,volume from stockquotes where symbol=\'SPY\' order by quotedate limit 250'),
    cnx, index_col="quotedate")
ax = plot_candlestick(df)

print(ax)

# plt.tight_layout()
plt.show()
