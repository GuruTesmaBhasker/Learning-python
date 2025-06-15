class carr:
    
    def __init__(self , wheels , milage , airbags): # Constructor
        print("THis is a constructor")
    
        self.wheels = wheels
        self.milage = milage
        self.airbags = airbags
    
    def __del__(self): # Destructor
        print("This is destrutor",self)
        
    def forward(self):#The self word could be anything like it can be Aself for everything 
        print("The car is moving forward")
        
    def backward(self):
        print("The car is moving backward")
        
    
car1= carr(6, 45, 6) # A object is created or called as Instance of class = Instantiation 
print(car1.wheels)
print(car1.milage)
print(car1.airbags)
print()
 

car2=carr(8,60 , 8)
print(car2.wheels)
print(car2.milage)
print(car2.airbags) #Prints the same value of car1
print()
#we need to change the value of the car2
car2.wheels=5
car2.milage=34
car2.airbags=4
#Now prints the updated value
print(car2.wheels)
print(car2.milage)
print(car2.airbags)

# Calling methods of the class
car1.forward()
car2.backward()