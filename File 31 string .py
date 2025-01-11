#creating a string 
name1 = 'Hello world 1'
name2 = "Hello world 2"
name3 = '''Hello 
world 
3 ''' #->> multiline string with triplequotes
print(name1,name2,name3)
print(name1[0]) #->> same as array
print(name2[-1]) 

#find a char/substring in a string
print(name1.find('i')) #->> if -1 is answer so char not present
print(name2.find('o'))
print(name2.find('llo'))

#slicing a string
#syntx->> [start:end] ->> start is included and end is excluded
print(name1[0:4])

#for converting string to upper case
print(name1.upper())

#for converting string to lower case
print(name1.lower())

#for capitalising the first character of string
print(name1.capitalize())

#for stripping/removing any trailing whitespaces
str = ("   hello world!!!    ")
print(str.strip())

#to replace a string ->> string.replace(old string,new string,count)
print(str.replace("hell","yele",1))
string = ("hello world what a beautiful world")
print(string.replace("world","earth",1))  #count tell how many words to replace

#to split string
print(name1.split())
print(name1.split("e",)) #->> e is separator here ->> string.split(separator, max slipt)
print(name1.split("l",2)) # 2 times separate

#concatenation 
str1 = "hello guys "
str2 = "what a great day"
print(str1 + str2)

#string formatting
student = "Ajay kumar"
marks = 98

stri = "student name is {s}, and student marks are {m}".format(s= student,m= marks)
print(stri)

# if have to print AK's house
house = "AK's house"
print(house)