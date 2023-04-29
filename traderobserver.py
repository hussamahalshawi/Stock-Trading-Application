from observer import Observer


class TraderObserver(Observer):
    def __init__(self,trader):
        self.trader = trader

    def update(self, prices):
        for symbol, price in prices.items():
            for stock in self.trader.portfolio.stocks:
                if stock.symbol == symbol:
                    stock.price = price
            