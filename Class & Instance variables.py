class Car:
    # Class variable (shared across all instances)
    wheels = 4

    def __init__(self, brand, mileage):
        # Instance variables (unique to each object)
        self.brand = brand
        self.mileage = mileage

    # Instance method (uses instance variables)
    def display_info(self):
        print(f"Brand: {self.brand}, Mileage: {self.mileage}, Wheels: {Car.wheels}")

    # Static method (does not use instance or class variables)
    @staticmethod # To print this we dont even need a object of the class
    def car_type():
        print("Car type: Sedan")

# Example usage
car1 = Car("Toyota", 23)
car2 = Car("Honda", 18)

# Accessing instance variables
car1.display_info()  # Output: Brand: Toyota, Mileage: 23, Wheels: 4
car2.display_info()  # Output: Brand: Honda, Mileage: 18, Wheels: 4

# Accessing class variable
print(Car.wheels)  # Output: 4

# Modifying class variable
Car.wheels = 6
car1.display_info()  # Output: Brand: Toyota, Mileage: 23, Wheels: 6
car2.display_info()  # Output: Brand: Honda, Mileage: 18, Wheels: 6
car1.wheels = 5  # This will not change the class variable, but create an instance variable for car1
car2.wheels = 7  # This will not change the class variable, but create an instance variable for car2


# Calling static method
Car.car_type()  # Output: Car type: Sedan