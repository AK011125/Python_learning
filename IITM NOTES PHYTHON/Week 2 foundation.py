# Notes  IITM Python lecture week 2

a=10 #if want to delete a then use del a
print(a)

print('it\'s a good day') #if you want to print single quotes, then enclose it within double quotes. or \'
print("I am from \"IITM\" college") #if you want to print double quotes, then enclose it within single quotes. or \"
b = '''First line
Second line
Third line'''
print(b)  #if you want to print multiple lines, then use triple quotes ''' ''' or """ """
'''First line
Second line
Third line''' #this will not print the output, as it is not assigned to any variable or '''''' is used to comment multiple lines

# if else question
marks = int(input("Enter the marks : "))
if marks >= 90  and marks <= 100:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif marks >= 70 and marks < 80:
    print("Grade C")
elif marks >= 60 and marks < 70:
    print("Grade D")
elif marks >= 50 and marks < 60:
    print("Grade E")
elif marks >= 0 and marks < 50:
    print("Fail")
else :
    print("Invalid marks")

import math
print(math.sqrt(25)) #5.0
print(math.pow(2,3)) #8.0
print(math.pi) #3.141592653589793
print(math.e) #2.718281828459045
print(math.sin(90)) #0.8939966636005579
print(math.cos(0)) #1.0
print(math.tan(45)) #1.6197751905438615
print(math.log(10)) #2.302585092994046
print(math.log10(10)) #1.0
print(math.exp(2)) #7.3890560989306495
print(math.factorial(5)) #120
 
import random 
a = random.random() #random number between 0 and 1
print(a) 
print(random.randrange(1,7)) #random number between 1 and 6 --> 1,2,3,4,5,6 Dice
dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
sum = dice1 + dice2
print(sum) #sum of two dice

import calendar
print(calendar.month(2024, 9)) #print the calendar of the month
print(calendar.calendar(2024)) #print the calendar of the year

from calendar import calendar
print(calendar(2024)) #print the calendar of the year