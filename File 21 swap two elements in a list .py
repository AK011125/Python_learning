n = int(input("Enter the length of list : "))
list = []

for i in range(n):
    n = int(input())
    list.append(n)

idx1 = int(input("Enter idx1 : "))
idx2 = int(input("Enter idx2 : "))
print(list)

# swapping two numbers
temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)