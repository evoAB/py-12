a=int(input("Enter a  number : "))
flag=0
for i in range(2,int(a/2+1)):
    if a%i==0:
        flag=1
        break

print("Number is prime") if flag==0 else print("Number is not prime")