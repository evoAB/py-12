a,b=int(input("Enter starting number ")),int(input("Enter ending number "))
print("Prime numbers under 100 : ",end=' ')
for i in range(a,b+1):
    flag=0
    for j in range(2,int(i/2+1)):
        if i%j==0:
            flag=1
    if(flag==0):
        print(i,end=' ')
            