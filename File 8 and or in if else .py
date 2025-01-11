eng_marks = int(input("Enter english marks : "))
hindi_marks = int(input("Enter hindi marks : "))

if eng_marks > 80 and hindi_marks > 80 :
    print(" A Grade ")
elif eng_marks > 80 or hindi_marks >80 :
    print(" B Grade ")
else :
    print(" C Grade ")