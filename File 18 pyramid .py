n = int(input("Enter a number : "))
for i in range (1,n+1):
    for j in range (1,n-i+1):  # to print space
        print(" ", end="")
    for k in range (1,2*i):    # to print number
        print(k, end="")
    print()