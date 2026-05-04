#counting even numbers in list
list=[2,3,4,5,6,7]
count=0

for num in list:
    if num%2==0:
        count+=1

print(f"total number of even elemnts is:{count}")