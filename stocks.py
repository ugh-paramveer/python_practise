#dictonary storing stocks and their prices

portfolio={}
used_budget=0
budget=float(input("enter your budget :"))
for i in range(3):
    
    stock=input("enter the name of the stock:")
    percent=int(input("enter allocation percentage:"))
    price=float(input("enter the price:"))
    amount=(percent/100)*budget

    
    if used_budget+amount>budget:
        print("budget exceeds")
        print("remaning budget=",budget-used_budget)
        break
   
    share=amount/price

    portfolio[stock]={
        "amount":amount,
        "shares":share,
        "percent":percent
    }
    used_budget+=amount


print("\nportfolio summary:")

for stock in portfolio:
    print(stock)
    print(" Investment:", portfolio[stock]["amount"])
    print(" Shares:", portfolio[stock]["shares"])
    print(f"percentage={portfolio[stock]["percent"]}%")

print("\nTotal used:", used_budget)
print("Remaining:", budget - used_budget)