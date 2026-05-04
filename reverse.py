#to reverse a list
list=[2,3,4,5,6,7]
revsrse=[]
for i in range(len(list)-1,-1,-1):#include step as well -1 stops at 0
    revsrse.append(list[i])

print(revsrse)
