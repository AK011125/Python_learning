# GrPa 1 Week 1 and some extra 
num = input()
first, middle, last = int(num[0]), int(num[1]), int(num[2]) #-->> int: Get the first, middle and last digit of the number as integers
if first + last == middle:
    print('sandwich')
else:
    print('plain')

# GrPa 2 Week 1 and some extra
# \ -->> is used to escape the next character
print("Double forward slash // and Double backward slash \\\\")

# GrPa 3 Week 1 and some extra
# new_word = new_word[:-3] -->> remove last 3 characters 

# GrPa 4 Week 1 and some extra
operation = input().strip() # strip () is used to remove the leading and trailing spaces
# lower(operation) # lower() is used to convert the string to lower case 
# upper(operation) # upper() is used to convert the string to upper case
# operation = operation.lower() -->> convert the string to lower case
# operation = operation.upper() -->> convert the string to upper case
# operation = operation.strip().lower() -->> remove the leading and trailing spaces and convert the string to lower case
# operation = operation.strip().upper() -->> remove the leading and trailing spaces and convert the string to upper case
# round(3.14159,2) -->> round is use to round off the number to given decimal places

# GrPa 5 Week 1 and some extra
# print(f"{total_cost:.02f}") -->> print the total_cost with 2 decimal places
pi = 3.14159265359
print(f"The value of pi is approximately {pi:.2f}") #-->> print the value of pi with 2 decimal places