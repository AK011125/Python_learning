set = {"Pooja", "Ajay jakhar", "Tannu", "Harsh"} #duplicate values not allowed , immutable , unindexed
print(set)
print(len(set))
print(set)

#adding element in set 
set.add("Sonu")
print(set)

#adding a sequence in set
newnames = {"Priyanaka", "sheetal"} 
set.update(newnames)
print(set)

#remove a element in set
set.remove("Pooja")
print(set)
set.discard("Tannu") # it is different from remove bcz it does not throw error if element is not present in set
print(set)

#joining two sets
s1 = {'a','b','c'}
s2 = {'d','e','a'}

print(s1 , s2)
s3 = s1.union(s2)
print(s3) # duplicates will not be printed

s1.update(s2)
print(s1)

# intersection_update
s1.intersection_update(s2)
print(s1)

#keep only different values 
s1.symmetric_difference_update(s2)
print(s1)