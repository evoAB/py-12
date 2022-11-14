a,b=int(input("Enter first number ")),int(input("Enter second number "))
print("HCF of numbers : ",end='')
min = a if a<b else b
while 1:
    if a%min==0 and b%min==0:
        break
    min-=1
print(min)
            