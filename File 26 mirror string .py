input_string = input("Enter string : ")
n = int(input("Enter n : "))

#creating dictionary for mirror operations
alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse_alphabets = alphabets[::-1] 
dict1 = dict(zip(alphabets,reverse_alphabets))

#finding the part of string which we will do mirror
prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding mirror string
mirror = ""
for i in range(0,len(suffix)):
    mirror = mirror + dict1[suffix[i]]

#creating the final string
result =prefix + mirror
print(result)