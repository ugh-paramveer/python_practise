#tells how much stcks are added in our portfolio
portfolio={}
total=0
while True:
    stock = input("Enter stock name: ")
    price = float(input("Enter price: "))
    shares = int(input("Enter shares: "))

    portfolio[stock]={
        "price":price,
        "shares":shares
    }

    for stock in portfolio:
        r_price=portfolio[stock]["price"]
        n_share=portfolio[stock]["shares"]

        value=r_price*n_share
        
        total+=value
        

    
    print(f"total worth of portfolio={total}")
    

    ans=input("want to add stocks (y/n):")

    if ans.lower() == "n":
        break
    print("portfolio summary:")
    for stock in portfolio:
        r_price=portfolio[stock]["price"]
        n_share=portfolio[stock]["shares"]

        value=r_price*n_share

        precentage=(value/total)*100

        print(f"{stock} value: {value}")
        print(f"{stock} allocation: {precentage:.2f}%\n")

        print(f"Total Portfolio Value = {total}")



        

