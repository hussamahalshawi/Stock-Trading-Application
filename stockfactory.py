from stock import Stock
class StockFactory:
    __instance = None
    
    def __init__(self):
        if StockFactory.__instance != None:
            raise Exception("StockFactory is a Singleton!")
        else:
            StockFactory.__instance = self
              
    
    def get_instance():
        if StockFactory.__instance == None:
            StockFactory()
        return StockFactory.__instance
    
    
    def create_stock(self, symbol, name, price):
        stock = Stock(symbol, name, price)
        return stock        
