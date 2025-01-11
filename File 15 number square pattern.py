n = int(input("Enter a number : "))
for _ in range (n):
    for i in range (1,n+1):
        print(i,end="") # (end="")->> use to print in same row
    print()  # use to print in next row