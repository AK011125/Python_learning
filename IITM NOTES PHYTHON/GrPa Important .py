# GrPa 1 Week 1 and some extra

a = 4
b = 6
print(abs(a-b)) #->> abs is use to find absolute difference between two numbers
print(max(a,b)) #->> max is use to find maximum of two numbers
print(min(a,b)) #->> min is use to find minimum of two numbers
print(pow(a,b)) #->> pow is use to find a^b
print(pow(a,b,10)) #->> pow is use to find a^b mod 10
print(round(3.14159,2)) #->> round is use to round off the number to given decimal places


# GrPa 3 Week 1 and some extra
s = "hello pyhton"
course_code = "24t2cs1002" # 24 - year, t2 - term 2, cs1002 - course id

output1 = s[2] # str: get the third character of s
output2 = s[-4] # str: get the fourth last character of s
output3 = s[:3] # str: get the first 3 characters of s
output4 = s[::2] # str: get every second character of s
output5 = s[-3:] # str: get the last 3 characters of s
output6 = s[::-1] # str: get the reverse of s

# GrPa 4 Week 1 and some extra 
word1 = "Wingardium" # str
word2 = "Leviyosa" # str
word3 = "Silver" # str
sentence = "Learning python is fun"
n1 = 6 # int
n2 = 4 # int

output1 = word1 + " " + word2 # str: join word1 and word2 with space in between
output2 = word1[:4] + "-" + word2[-4:] # str: join first four letters of word1 and last four letters of word 2 with a hyphen "-" in between
output3 = word3 + " " + str(n1) # str: join the word3 and n1 with a space in between
output4 = "-" * 50 # str: just the hypen "-" repeated 50 times
output5 = "-" * n2 # str: just the hypen "-" repeated n2 times
output6 = str(n1) * n2 # str: repeat the number n1, n2 times
are_all_words_equal = word1 == word2 == word3 # bool: True if all three words are equal
is_word1_comes_before_other_two = word1 < word2 and word1 < word3 # bool: True if word1 comes before word2 and word3 assume all words are different
has_h = 'h' in word1 or 'H' in word1  # bool: True if word1 has the letter h
ends_with_a = word1[-1].lower() == 'a' # bool: True if word1 ends with letter a or A
has_the_word_python = "python" in sentence.lower() # bool: True if the sentence has the word python

# GrPa 5 Week 1 and some extra

age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:]) # int, int, int: Get the correct parts from dob as int
fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 
last_birthday = str(day)+"/"+str(month)+"/"+str(year+age) # str: last birthday formatted as day/month/year
month += 10
month, year = (month-1)%12+1, year+(month-1)//12
tenth_month = str(day)+"/"+str(month)+"/"+str(year) # str: dob same day after 10 months formatted as day/month/year
# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month,fifth_birthday,last_birthday, sep=", ")
weight = float(input()) # float: Read a number as float from stdin(Standard input)
kg = int(weight)  # Get the integer part (kg)
grams = int((weight - kg) * 1000)  # Get the fractional part converted to grams
weight_readable = str(kg)+" kg "+str(grams)+" grams" # str: reformat weight of format 55 kg 250 grams
# print weight_readable 
print(weight_readable)
