n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))

#Sum
print("Sum of numbers is : ",n1+n2)
#exponenitation
print("n1 power n2 is : ",n1**n2)
#floor divison operator
print("Nearest whole number is :",n1//n2)  #It will give us nearest whole number 
# + - * / % sabh arthematic ke jase he use hote hai

print("Subtraction : ",n1-n2)
print("Remainder is : ",n1%n2) #Modulus operator

#Comperision operator 
print(n1>n2) # It will print true or false

#Identity operator  (is is not)
x=2
y=2
print("if x is y", x is y)
print("if x is not y ", x is not y)

#Membership operator
fruits = ["banana","mango","apple"]
print("if orange is present in fruits : ","orange" in fruits )
print("if mango is present in fruits : ","mango" not in fruits )

#Bitwise operator 
a=3
b=4
print("a and b : ", a & b)
print("a or b : ", a | b)
print("a xor b : ", a ^ b)