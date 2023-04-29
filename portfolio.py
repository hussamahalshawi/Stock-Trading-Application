from stockmarket import StockMarket
class Portfolio:
    def __init__(self):
        self.stocks = [] # list of object to all stocks of portfolio
        self.stocks_buy = [] # list of object to all stocks buy of portfolio

    def add_stock(self, stock):
        self.stocks.append(stock)
    
    def add_stock_buy(self, stock):
        self.stocks_buy.append(stock)
        if stock in self.stocks:
            self.stocks.remove(stock)


    def remove_stock(self, stock):
        self.stocks.remove(stock)
    
    def remove_stock_buy(self, stock):
        self.stocks_buy.remove(stock)
        self.stocks.append(stock)
