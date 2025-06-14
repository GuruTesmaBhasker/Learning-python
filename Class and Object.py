# Object Oriented Programming in Python
# Class is a blueprint for creating objects
# Object is an instance of a class

# A simple class and object example
class car:
    wheels=4
    milage=23
    airbags=2
    
    def forward(self):
        print("The car is moving forward")
        
    def backward(self):
        print("The car is moving backward")
        
car1= car() # A object is created or called as Instance of class = Instantiation 
print(car1.wheels)
print(car1.milage)
print(car1.airbags)
print()


car2=car()
print(car2.wheels)
print(car2.milage)
print(car2.airbags) #Prints the same value of car1
print()

#we need to change the value of the car2
car2.wheels=5
car2.milage=34
car2.airbags=4
# Now car2 has different values than car1
# Now prints the updated value
print(car2.wheels)
print(car2.milage)
print(car2.airbags)

# Calling methods of the class
car1.forward()
car2.backward()