import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import os

def plt_stock(df: pd.DataFrame):
    df_ohlc = df[['Open', 'High', 'Low', 'Close']]

    # Apply smoothing with simple moving average
    legend = ['Moving Average (10)']
    smooth = df['Close'].rolling(window=10).mean()
    add_plots={
        'Moving Average (10)' : mpf.make_addplot(smooth, color='orange')
    }

    fig, ax = mpf.plot(df_ohlc, type='candle', style='charles', title='AAPL', addplot=list(add_plots.values()), returnfig=True)

    ax[0].legend([None]*(len(add_plots)+2))
    handles = ax[0].get_legend().legendHandles
    ax[0].legend(handles=handles[2:],labels=list(add_plots.keys()))

dir_archive = os.path.join(os.curdir, 'archive')
dir_test = os.path.join(dir_archive, 'AAPL_2006-01-01_to_2018-01-01.csv')
df_test = pd.read_csv(dir_test, index_col=0, parse_dates=True)


plt_stock(df_test)
mpf.show()
