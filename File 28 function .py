def studentinfo (**kwargs):
    for x,y in kwargs.items():
        print(x ,"is", y)

studentinfo(name= "Urvi",age="22",city="Delhi")
studentinfo(name="Ajay",age="20",city="Jhajjar")

#pass by value ->> immutable ->> string,tuple,integer,float
def addone (x):
    x=x+1
    print("Inside value is : ",x)

x=5
addone(x)
print("Outside value is : ",x)

#pass by reference ->> mutable ->> list,dictionary

def modifylist(list):
    list.append(4)
    print("Inside list : ",list)

list = [1,2,3]
modifylist(list)
print("Outside list : ",list)