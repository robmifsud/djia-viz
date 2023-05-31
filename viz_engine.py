import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import os

def plt_stock(df: pd.DataFrame):
    df_ohlc = df[['Open', 'High', 'Low', 'Close']]

    # Apply smoothing with simple moving average
    legend = [
        'Resistance Trend',
        'Support Trend',
        'Moving Average (10)'
    ]

    smooth = df['Close'].rolling(window=10).mean()
    add_plots=[
        mpf.make_addplot(smooth, color='orange')
    ]

    # Trend lines 2011-12-16 to 2013-12-13
    dates=[
        '2011-11-25',
        '2012-04-10',
        '2012-05-18',
        '2012-09-21',
        '2012-11-16',
        '2012-12-03',
        '2013-04-19',
        '2013-05-07',
        '2013-06-28',
        '2013-12-19'
    ]

    datepairs = [(dates[i], dates[i+1]) for i in range(0,9)]

    tlines_list = [
        dict(tlines=datepairs, tline_use='high', colors='r'),
        dict(tlines=datepairs, tline_use='low', colors='g')
    ]

    fig, ax = mpf.plot(df_ohlc, type='candle', style='charles', title='AAPL', addplot=add_plots, returnfig=True, tlines=tlines_list)

    ax[0].legend([None]*(3+2))
    handles = ax[0].get_legend().legendHandles
    ax[0].legend(handles=handles[2:],labels=legend)

dir_archive = os.path.join(os.curdir, 'archive')
dir_test = os.path.join(dir_archive, 'AAPL_2006-01-01_to_2018-01-01.csv')
df_test = pd.read_csv(dir_test, index_col=0, parse_dates=True)


plt_stock(df_test)
mpf.show()
