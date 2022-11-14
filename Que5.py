a=int(input("Enter a number "))
print("Next prime number : ")
while 1:
    flag=0
    a+=1
    for i in range(2,int(a/2+1)):
        if(a%i==0):
            flag=1
            break
    if(flag==0):
        print(a)
        break
            