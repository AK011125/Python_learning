#Find the Factorial of a given number 
n = int(input("Enter a number : "))
fact = 1
if n >=0 :
    for i in range (1,n+1) :  # range (initaial ; termination)
        fact = fact * i
        i = i+1
    print(fact)
else : print("Not defined")