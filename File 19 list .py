fruits = ["apple", "mango", "banana", "cherry"]
print(fruits) #printing list
print(type(fruits)) #type
print(len(fruits)) #length of list

#checking a element present in a list or not
if "banana" in fruits :
    print("Present in list")

#indexing in list
print(fruits[1])
print(fruits[-3])
print(fruits[-3:-1])
print(fruits[1:8])

#adding elements to a list 
fruits.append("kiwi")
print(fruits)

fruits.insert(3, "cherry")
print(fruits)

more_fruits =["cherry","oranges"]
fruits.extend(more_fruits)
print(fruits)

#removing elements from list 
fruits.remove("banana")
print(fruits)

fruits.pop(1) 
print(fruits)

fruits.pop()  #if index is not given so it remove last element
print(fruits)

#changing element of list
fruits[1] = "papaya"
print(fruits)

fruits[1:3] = ["oranges","tomato","gavava"]
print(fruits)

#sorting a list
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)