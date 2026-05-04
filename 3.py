#to print the longest name 
list=["param","ssodhi","viratkholi"]
largest=list[0]

for name in list:
    if len(name) > len(largest):
        largest=name

print(largest)  