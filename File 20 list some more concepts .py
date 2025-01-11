#list comprehansion
num = [10,20,30,40,50,60,70,80,90]
fruits = ["apple","banana","papaya","cherry","oranges","kiwi"]
newlist = [i for i in num if i> 25]
print(newlist)

newfruits = [i for i in fruits if "a" in i]
print(newfruits)

#copy a list 
freshfruits = fruits.copy()
print(freshfruits)

freshfruits = fruits + freshfruits
print(freshfruits)

#nested list 
fruits.insert(2, ["gavava","pinapple"])
print(fruits)
print(fruits[2][1]) # use two brackets for nested list 