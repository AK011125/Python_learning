n = int(input("Enter the number : "))

def factorial (n):
    ans = 1
    if n ==0 :
        ans = 1
    else:
        for i in range (1,n+1):
            ans=ans*i
    return ans 

output = factorial(n)
print("The factorial is : ",output)