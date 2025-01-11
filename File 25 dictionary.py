# creating dictionary 
phone = {
    "Ajay" : 8753873,
    "Pooja" : 887587,
    "Tannu" : 346663,
    "Harsh" : 355759,
}

#printing dictionary 
print(phone)

#checking type
print(type(phone))

#check the length
print(len(phone))

#access item
print(phone["Ajay"])
print(phone.get("Pooja"))
print(phone.keys())

#update value in dictionary
phone["Ajay"] = 967188
print(phone)

#add element
phone["sonu"] = 57546
print(phone)

more_phones = {
    "Priyanka" : 868796
}
phone.update(more_phones)
print(phone)

#removing items
phone.pop("Pooja")
print(phone)

phone.popitem() #this will remove last item
print(phone)

# phone.clear() to clear the dictionary

#printing values of a dictionary
for x in phone.items():
    print(x)

#nested dictionary 
phones = {
    "Area 1" : {
        "x" : 32,
        "y" : 43,
        "z" : 33
    },
    "Area 2" : {
        "a" : 39,
        "b" : 75,
        "c" : 45
    }
}
print(phones["Area 1"]["y"])
print(phones["Area 2"]["c"])