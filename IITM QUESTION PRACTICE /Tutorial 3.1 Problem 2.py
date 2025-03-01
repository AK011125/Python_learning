# find the number of digits in the given number
n = abs(int(input("Enter a number : ")))
count = 1
while (n >9) :
    n = n//10
    count = count + 1
print(count)