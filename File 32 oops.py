class rectangle :
    def dimensions(self,height,breadth):
        self.height = height
        self.breadth = breadth

    def area(self):
        return self.height*self.breadth 
    
    def perimeter(self):
        return 2*(self.height+self.breadth)
    
h = int(input("Enter height : "))
b = int(input("Enter breadth : "))

#creating objects 
rectangle1 = rectangle()
rectangle1.dimensions(h,b)
print("The height of rectangle is : ",h ,"The breadth of rectangle is : ",b)
print("The area of rectangle is : ",rectangle1.area())
print("The perimeter of rectangle is : ",rectangle1.perimeter())