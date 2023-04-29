from observer import Observer

class StockObserver(Observer):
    def __init__(self,stock):
        self.stock = stock

    def update(self, prices):
        for symbol, price in prices.items():
            if self.stock.symbol == symbol:
                print(f"Price of {self.stock.symbol} has changed to {price}. Notifying traders...")
