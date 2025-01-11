# def function_name (parameter):
#    body statement
#    return expression 


# function to find sum of two numbers 
def sum (n1,n2):
    answer = n1+n2
    return answer

#calling a function
# function_name (argument1,argument2)

x=3
y=6
ans=sum(x,y)
print("sum of",x,"and",y,"is : ",ans)

#positional argument and named/keyword argument ->> sum(2,3)  sum(n1=2,n2=3)
#sum(*args) ->> we can pass as many arguments as we want now