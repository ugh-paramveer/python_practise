# Program to find sum of first N numbers
def add(n):
    if n==0:
        return 1
    return n + add(n-1)


n=int(input("enter the number ="))
print(add(n))
