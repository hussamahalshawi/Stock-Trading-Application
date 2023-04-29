from stockfactory import StockFactory
from stockmarket import StockMarket
from portfolio import Portfolio
from trader import Trader
from stockobserver import StockObserver
from traderobserver import TraderObserver




if __name__ == '__main__':
    # Create a StockFactory object
    factory = StockFactory.get_instance()

    # Create some sample stocks
    apple_stock = factory.create_stock('AAPL', 'Apple Inc.', 130.21)
    google_stock = factory.create_stock('GOOG', 'Google Inc.', 2069.66)
    microsoft_stock = factory.create_stock('MSFT', 'Microsoft Corporation', 235.75)
    # Create a StockMarket object and add the stocks to it
    stock_market = StockMarket()
    stock_market.add_stock(apple_stock)
    stock_market.add_stock(google_stock)
    stock_market.add_stock(microsoft_stock)
    
    # stock_market.remove_stock(google_stock)
    # stock_market.remove_stock(microsoft_stock)

    print("\n---------------------all stocks before update-------------------------------------")
    # Output the stocks portfolio
    for stock in stock_market.stocks:
        print(stock.symbol, stock.name, stock.price)

    # Create a Portfolio object and add some stocks to it
    portfolio = Portfolio()
    if apple_stock in stock_market.stocks:
        portfolio.add_stock(apple_stock)
    if google_stock in stock_market.stocks:
        portfolio.add_stock(google_stock)


    print("\n---------------------portfolio before update--------------------------------------")
    # Output the trader's portfolio
    for stock in portfolio.stocks:
        print(stock.symbol, stock.name, stock.price)
    


    # Create a Trader object and link it to the portfolio
    trader = Trader(portfolio)
    if google_stock in stock_market.stocks:
        trader.buy_stock(google_stock)

    print("\n---------------------stocks show--------------------------------------------------")
    # Output the trader's portfolio
    for stock in portfolio.stocks:
        print(stock.symbol, stock.name, stock.price)
    
    
    print("\n---------------------stocks buy---------------------------------------------------")
    # Output the trader's portfolio
    for stock in portfolio.stocks_buy:
        print(stock.symbol, stock.name, stock.price)
    
    # if google_stock in stock_market.stocks:
    #     trader.sell_stock(google_stock)


    
    # Create TraderObservers and StockObserver for the trader's stocks and add them to the StockMarket
    for stock in trader.portfolio.stocks:
        trader_observer = TraderObserver(trader)
        stock_observer = StockObserver(stock)
        stock_market.add_trader_observer(trader_observer)
        stock_market.add_stock_observer(stock_observer)

    for stock in trader.portfolio.stocks_buy:
        trader_observer = TraderObserver(trader)
        stock_observer = StockObserver(stock)
        stock_market.add_trader_observer(trader_observer)
        stock_market.add_stock_observer(stock_observer)

    print("\n---------------------notify update 1------------------------------------------------")
    prices = {}
    stock_market.update_prices(prices)
    
    
    print("\n---------------------notify update 2------------------------------------------------")
    prices = {'GOOG': 2100.66}
    stock_market.update_prices(prices)

    print("\n---------------------notify update 3------------------------------------------------")
    # Update the prices of the stocks in the StockMarket
    prices = {'AAPL': 140.21, 'GOOG': 2300.66, 'MSFT': 250.75}
    stock_market.update_prices(prices)

    print("\n---------------------portfolio after update-----------------------------------------")
    # Output the stocks updated portfolio
    for stock in trader.portfolio.stocks:
        print(stock.symbol, stock.name, stock.price)

    for stock in trader.portfolio.stocks_buy:
        print(stock.symbol, stock.name, stock.price)

    print("\n---------------------all stocks after update----------------------------------------")
    # Output the stocks portfolio
    for stock in stock_market.stocks:
        print(stock.symbol, stock.name, stock.price)
