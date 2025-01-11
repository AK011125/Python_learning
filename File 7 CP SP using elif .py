cp = int(input("Enter the cost price : "))
sp = int(input("Enter the selling price : "))

if cp > sp :
    print("Loss of amount : ",cp-sp)
elif sp > cp:
    print("Profit of amount : ",sp-cp)  #elif is used for else if
else :
    print("No profit no loss ")