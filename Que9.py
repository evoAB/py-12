a,b=int(input("Enter first number ")),int(input("Enter second number "))
print("LCM of numbers : ",end='')
max = a if a>b else b
while 1:
    if max%a==0 and max%b==0:
        break
    max+=1
print(max)
            