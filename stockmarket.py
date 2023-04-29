class StockMarket:
    def __init__(self):
        self.stocks = [] # list of object to all stocks
        self.stock_observers = []
        self.trader_observers = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def add_stock_observer(self,stock_observer):
        self.stock_observers.append(stock_observer)

    def add_trader_observer(self,trader_observer):
        self.trader_observers.append(trader_observer)

    def notify_stock(self, prices):
        for observer in self.stock_observers:
            observer.update(prices)

    def update_trader(self, prices):
        for observer in self.trader_observers:
            observer.update(prices)

    def update_prices(self, prices):
        for symbol, price in prices.items():
            for stock in self.stocks:
                if stock.symbol == symbol:
                    stock.price = price
        self.update_trader(prices)
        self.notify_stock(prices)