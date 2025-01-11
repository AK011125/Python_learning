# creating a tuple 
colors = ("blue","green","red")  #immutable ->> change nhi kar sakte 

# creating a tuple with single element
fruit = ("apple",) # extra comma aayega

# checking type of tuple
print(type(fruit))

# define tuple in differ way
fruits = tuple(("cherry", "banana" , "apple"))
print(fruits)

# checking length of tuple 
print(len(fruits))

# accessing element of tuple
print(colors[0]) #positive indexing
print(colors[-3]) #negative indexing
print(colors[1:3]) #range indexing
print(colors[-3:]) #negative range indexing

# checking if a item exits or not
if "blue" in colors :
    print("blue is present")

# traverse a tuple
for i in colors:
    print(i)

# concatenate 2 tuples
more_colors = ("green","orange")
colors = colors + more_colors
print(colors)

# Unpacking a tuple 
colour1 , colour2 , colour3  , colour4 , colour5 = colors #must be equal to number of items of tuple
print(colour1, colour2, colour3, colour4, colour5)