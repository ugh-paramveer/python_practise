class stocks:
    def __init__(self,name,price:float,shares:int,crr:float):
        self.name=name
        self.price=price
        self.shares=shares
        self.current_price=crr

    def value(self):
        return self.price*self.shares
    def profit_loss(self):
        return (self.current_price-self.price)*self.shares

class portfolio:
    def __init__(self):
        self.stocks={}
    def add_stock(self,stock):
        self.stocks[stock.name]=stock
    def total_value(self):
        total=0
        for s in self.stocks:
            obj=self.stocks[s]#need to pass object as it is stored like coke:{memoery adress}
            total+=obj.value()
        return total
    def show_allocation(self):
        value=0
        total=self.total_value()
        for s in self.stocks.values():# no need to pass obeject, with values()
             value=s.value()
             precentage=(value/total)*100
             print(f"{s.name} value: {value}")  

    def show_return(self):
        for s in self.stocks.values():
            Return=s.profit_loss()
            print(f"{s.name} profit/loss: {Return}")    
    def summary(self):
        print("\n--- Portfolio Summary ---")
        self.show_allocation()
        self.show_return()
        print("Total Value:", self.total_value())

p=portfolio()
s1=stocks("coke",60,10,70)
s2=stocks("coal",50,15,45)
p.add_stock(s1)
p.add_stock(s2)

p.summary()






