# Print numbers from 1 to 5 using a for loop
for i in range(1, 6):
    print(i)

# Python program to demonstrate range() function
# The range() function generates a sequence of numbers

# range(start, stop, step)
# Let's understand each parameter in the range function

# Start: The value where the sequence starts (inclusive)
# Stop: The value where the sequence ends (exclusive)
# Step: The difference between each number in the sequence

print("Using range(1, 10, 2):")
for i in range(1, 10, 2):  # Starts at 1, goes up to 9, increments by 2
    print(i)
    
# Output: 1 3 5 7 9

print("\nUsing range(0, 5):")
for i in range(0, 5):  # Starts at 0, ends before 5, default step is 1
    print(i)

# Output: 0 1 2 3 4

print("\nUsing range(10, 1, -2):")
for i in range(10, 1, -2):  # Starts at 10, ends before 1, decreases by 2
    print(i)

# Output: 10 8 6 4 2 


# Print numbers from 1 to 5 using while loop
i = 1
while i <= 5:
    print(i)
    i += 1
# Output: 1 2 3 4 5