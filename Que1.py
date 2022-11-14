a=int(input("Enter a number : "))

print("Reverse number : ",end='')
while a:
    print(a%10,end='')
    a=int(a/10)