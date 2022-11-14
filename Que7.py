a,b=int(input("Enter first number of pair : ")),int(input("Enter second number of pair : "))
flag=0
for i in range(2,int(a/2+1) if a>b else int(b/2+1)):
    if a%i==0 and b%i==0:
        flag=1
        break

print("Number is co-prime") if flag==0 else print("Number is not co-prime")
