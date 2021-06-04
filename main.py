import yfinance as yf
import matplotlib.pyplot as plt


def stock_graph():
    print("Please enter the stock ticker you would like to see information for:")
    inputs = input().upper()

    tick = yf.Ticker(inputs)

    prices = tick.history(start='2020-06-03', end='2021-06-03').Close
    prices = prices.to_frame()

    sma5 = prices.Close.rolling(window=5).mean()
    sma20 = prices.Close.rolling(window=20).mean()
    sma50 = prices.Close.rolling(window=50).mean()
    sma100 = prices.Close.rolling(window=100).mean()

    plt.plot(prices, label=inputs)

    print("Would you like to plot a 5 day SMA?")
    inputs = input().upper()
    if inputs == 'Y' or inputs == 'YES':
        plt.plot(sma5, label=inputs + ' 5 Day SMA', color='orange')

    print("Would you like to plot a 20 day SMA?")
    inputs = input().upper()
    if inputs == 'Y' or inputs == 'YES':
        plt.plot(sma20, label=inputs + ' 20 Day SMA', color='magenta')

    print("Would you like to plot a 50 day SMA?")
    inputs = input().upper()
    if inputs == 'Y' or inputs == 'YES':
        plt.plot(sma50, label=inputs + ' 50 Day SMA', color='red')

    print("Would you like to plot a 100 day SMA?")
    inputs = input().upper()
    if inputs == 'Y' or inputs == 'YES':
        plt.plot(sma100, label=inputs + ' 100 Day SMA', color='green')

    plt.legend(loc='upper left')
    plt.ylabel('Price in USD')
    plt.xlabel('Date')
    plt.show()


def cycle():
    stock_graph()
    print("Would you like to view more stocks? (Y/N)")
    inputs = input().upper()

    while inputs != "Y" and inputs != "N":
        print("Please enter Y/N")
        inputs = input().upper()

    if inputs == "Y":
        cycle()


cycle()
