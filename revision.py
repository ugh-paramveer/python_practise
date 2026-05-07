#Problem #4 — combines everything so far
#You have a list of transactions. Find the top 3 spenders and return their names and total spend.

def sort(set)->dict:
    sorted_list={}
    for item in set:
        name=item["name"]
        price=item["amount"]
        if name not in sorted_list:
            sorted_list[name]=price
        elif name in sorted_list :
            sorted_list[name]+=price
    return sorted_list


    
transactions = [
    {"name": "Param", "amount": 200},
    {"name": "Raj",   "amount": 150},
    {"name": "Param", "amount": 350},
    {"name": "Priya", "amount": 900},
    {"name": "Raj",   "amount": 400},
    {"name": "Amit",  "amount": 100},
    {"name": "Priya", "amount": 200},
    {"name": "Amit",  "amount": 800},
]

ans=sort(transactions)

ans1=sorted(ans,key=lambda x:x["name"],reverse=True)
print(ans1)


# ans1=rank(ans)
# print(ans1)


# Expected output:
# [("Priya", 1100), ("Amit", 900), ("Raj", 550)]