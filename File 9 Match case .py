#  Switch case jesa he hai 
# # match x :
# case "1": statement 
# case "2": statement 
# case "3": statement 
# case _: default statement 

n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))

operator = input("Enter a operator : ")

match operator :
    case "+" : print(n1 + n2)
    case "-" : print(n1 - n2)
    case "*" : print(n1 * n2) 
    case "/" : print(n1 / n2)
    case _ : print("Invalid operator")