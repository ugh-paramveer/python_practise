stock={}

name=input("enter the name of stock:")
price=float(input("enter the price of stock:$"))
eps=float(input("enter the eps:$"))
eps_growth=float(input("enter the annual growth rate of eps (10 years, in % ):"))
bv=float(input("enter the book value:$"))
bv_growth=float(input("enter the annual growth rate of book value (10 years, in % ):"))
low_pe=float(input("enter the historicly  lowest p/e of the stock:"))

stock[name]={
    "price":price,
    "eps":eps,
    "eps_growth":eps_growth,
    "book_value":bv,
    "bv_growth":bv_growth,
    "low_pe" : low_pe
}

return1=stock[name]["eps"]/stock[name]["book_value"]*100
return2=stock[name]["eps"]/stock[name]["price"]*100
fv_eps=(stock[name]["eps"]*(1+(stock[name]["eps_growth"]/100))**10)
fv_bv=(stock[name]["book_value"]*(1+(stock[name]["bv_growth"]/100))**10)
fv_return1=(fv_eps/fv_bv)*100
fv_price=fv_eps*stock[name]["low_pe"]
fv_return2=(fv_eps/fv_price)*100
cmp_rate = (((fv_price / stock[name]["price"]) ** (1/10)) - 1) * 100

print(f"{'='*50}")
print(f"its producing  annual rate of return of {return1:.2f}% with book value ")
print (f"its actual annual rate of return of {return2:.2f}%  ")
print(f"annual rate of return of 10 years can be:{fv_return1:.2f}% with book value ")
print(f"annual rate of return of 10 years can be:{fv_return2:.2f}% ")
print(f"total gains could be ${fv_price-stock[name]['price']} ")#cannot use "price" instead 'price'
print(f"total rate of return:{((fv_price-stock[name]['price'])/stock[name]['price'])*100}%")
print(f"compounding annual rate of return:{cmp_rate}")












