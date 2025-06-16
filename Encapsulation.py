#Encapsulation in Python
# Encapsulation is a fundamental concept in object-oriented programming that restricts direct access to an object's attributes and methods.
# It allows for data hiding and abstraction, ensuring that the internal representation of an object is hidden from the outside.

class Car:
    def __init__(self, wheels, mileage, airbags):
        self.__wheels = wheels  # Private attribute
        self.__mileage = mileage  # Private attribute
        self.__airbags = airbags  # Private attribute

    def get_wheels(self):
        return self.__wheels  # Getter for wheels
        # Getters and setters are methods that allow controlled access to private attributes.
        # Getter is used to retrieve the value of a private attribute

    def set_wheels(self, wheels):
        if wheels > 0:
            self.__wheels = wheels  # Setter for wheels
            # Setter is used to set or update the value of a private attribute.
        else:
            print("Invalid number of wheels")

    def get_mileage(self):
        return self.__mileage  # Getter for mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage  # Setter for mileage
        else:
            print("Invalid mileage")

    def get_airbags(self):
        return self.__airbags  # Getter for airbags

    def set_airbags(self, airbags):
        if airbags >= 0:
            self.__airbags = airbags  # Setter for airbags
        else:
            print("Invalid number of airbags")

    def forward(self):
        print("The car is moving forward")
    def backward(self):
        print("The car is moving backward")

# Example usage
car1 = Car(4, 25, 2)  # Create an instance of Car
print("Wheels:", car1.get_wheels())
print("Mileage:", car1.get_mileage())
print("Airbags:", car1.get_airbags())

car1.set_wheels(6)  # Update wheels using setter
print("Updated Wheels:", car1.get_wheels())

car1.set_mileage(30)  # Update mileage using setter
print("Updated Mileage:", car1.get_mileage())

car1.set_airbags(4)  # Update airbags using setter
print("Updated Airbags:", car1.get_airbags())

# Calling methods of the class
car1.forward()
car1.backward()
# Attempting to access private attributes directly will raise an error
# print(car1.__wheels)  # This will raise an AttributeError
# print(car1.__mileage)  # This will raise an AttributeError

# Instead, use the getter methods to access private attributes
# print(car1.get_wheels())  # This will work
# print(car1.get_mileage())  # This will work

# Attempting to set private attributes directly will raise an error
# car1.__wheels = 5  # This will raise an AttributeError
# car1.__mileage = 35  # This will raise an AttributeError

# Instead, use the setter methods to update private attributes
# car1.set_wheels(5)  # This will work
# car1.set_mileage(35)  # This will work
# 
# print("Updated Wheels:", car1.get_wheels())  # This will work
# print("Updated Mileage:", car1.get_mileage())  # This will work

# The encapsulation ensures that the internal state of the Car object is protected and can only be modified through defined methods.