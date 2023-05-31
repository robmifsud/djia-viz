import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import os

def plt_stock(df : pd.DataFrame, date_range : tuple, trend_lines : tuple, title : str):
    # Unpack parameters
    start, end = date_range
    tl_up, tl_down = trend_lines

    # Create trend lines
    tlines_list = [
        dict(tlines=tl_up, tline_use='low', colors='g'),
        dict(tlines=tl_down, tline_use='high', colors='r')
    ]

    # Calculate volatility
    df['Volatility'] = df['Close'].rolling(window=50).std()

    # Apply smoothing with simple moving average
    df['Smooth'] = df['Close'].rolling(window=10).mean()

    # Add plots and limit to date range
    add_plots=[
        mpf.make_addplot(df['Smooth'].loc[pd.IndexSlice[start:end]], color='orange'),
        mpf.make_addplot(df['Volatility'].loc[pd.IndexSlice[start:end]], color='blue', panel=1, secondary_y=True)
    ]

    # Limit to date range
    df = df.loc[pd.IndexSlice[start:end]]

    fig, ax = mpf.plot(df, type='candle', style='charles', title=title, addplot=add_plots, returnfig=True, tlines=tlines_list)

    # Create legend
    legend_items = [
        plt.Line2D([], [], color='r', label='Resistance Trend'),
        plt.Line2D([], [], color='g', label='Support Trend'),
        plt.Line2D([], [], color='orange', label='Moving Average (window=10)'),
        plt.Line2D([], [], color='b', label='Volatility (window=50)')
    ]
    ax[0].legend(handles=legend_items)

dir_archive = os.path.join(os.curdir, 'archive')
dir_test = os.path.join(dir_archive, 'AAPL_2006-01-01_to_2018-01-01.csv')
df_test = pd.read_csv(dir_test, index_col=0, parse_dates=True)

datepairs_up = [
        ('2012-01-24', '2012-04-13'),
        ('2012-05-18', '2012-09-27'),
        ('2013-06-28', '2013-11-21'),
    ]

datepairs_down = [
    ('2012-04-25', '2012-05-16'),
    ('2012-10-04', '2013-04-25'),
]

plt_stock(df=df_test, date_range=('2011-12-16','2013-12-13'), trend_lines=(datepairs_up, datepairs_down), title='AAPL')
mpf.show()
