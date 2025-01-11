n = int(input("Enter a number : "))

for i in range(1,n+1):
    a=1
    a=a+64
    for j in range(1,i+1):
        print(chr(a), end="")
        a=a+1
    print()