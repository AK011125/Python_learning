#for i in range(Initialisation,termination,step) ->> for i in range(1,10,2)->> 1,3,5,7,9
for i in range(1,10):
    print(i,"Hello world")

for i in range(1,10,2):
    print(i,"Hello world")

for i in range(10): # it will take 10 at termination point and 0 as initialisation
    print(i,"Hello world")

for _ in range(10): # 10 times hello world only 
    print("Hello world")