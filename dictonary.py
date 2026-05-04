#dictonary storing stocks and their prices

portfolio={}
budget=int(input("enter your budget :"))
for i in range(3):
    name=input("enter the name of the stock:\n")
    percent=int(input("enter allocation percentage:\n"))
    
    amount=(percent/100)*budget
    
    portfolio[name]=amount


print("\nBudget Allocation:")

for stock in portfolio:
    print(stock, ":", portfolio[stock])