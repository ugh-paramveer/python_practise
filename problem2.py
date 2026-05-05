# Problem #2 — Stock Filter
# Given a list of stocks, return only the ones worth buying based on Buffett's basic rule: ROE above 15% AND earnings yield above 5%.

def result(stocks:list[dict])->list:
    result=[]
    for items in stocks :
        name=items["name"]
        eps=items["eps"]
        bv=items["bv"]
        price=items["price"]
        roe=(eps/bv)*100
        earning=(eps/price)*100
        print(name,roe,earning)
        if roe>=15 and earning >= 5:
            result.append(name)
        else:
            continue

    return result

        



stocks = [
    {"name": "Coke",   "eps": 2.50, "bv": 12.0, "price": 60.0},
    {"name": "Apple",  "eps": 6.00, "bv": 4.0,  "price": 185.0},
    {"name": "Ford",   "eps": 1.20, "bv": 15.0, "price": 40.0},
    {"name": "Visa",   "eps": 8.50, "bv": 35.0, "price": 230.0},
]

r=result(stocks)
print(r)

# ROE = eps / bv * 100
# Earnings Yield = eps / price * 100