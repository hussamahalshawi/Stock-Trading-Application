class Trader:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def buy_stock(self, stock):
        self.portfolio.add_stock_buy(stock)

    def sell_stock(self, stock):
        self.portfolio.remove_stock_buy(stock)
    
