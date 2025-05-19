# Get user's age as input
age = int(input("Enter your age: "))

# Conditional statements to classify the age group
if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
elif age >= 20 and age <= 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# User inputs
# Get user's age as input (currently unused in the logic)
age = int(input("Enter your age: "))  # Input for age (currently unused in the logic)
eat_pizza = input("Do you eat pizza? (YES/NO): ").strip().upper() == "YES"  # Converts input to boolean
exercise = input("Do you exercise? (YES/NO): ").strip().upper() == "YES"   # Converts input to boolean

# First condition: if eat_pizza and not exercise
if eat_pizza and not exercise:
    # eat_pizza = True (1), exercise = False (0), not exercise = True (1)
    # True and True = True (1), so this block will execute
    print("Unfit")

# Second condition: elif not eat_pizza and exercise
elif not eat_pizza and exercise:
    # eat_pizza = False (0), not eat_pizza = True (1), exercise = True (1)
    # True and True = True (1), so this block will execute
    print("Fit")

# Third condition: elif eat_pizza and exercise
elif eat_pizza and exercise:
    # eat_pizza = True (1), exercise = True (1)
    # True and True = True (1), so this block will execute
    print("Balanced - Pizza lover but healthy!")

# Final else block if none of the above conditions are true
else:
    # This block is executed if none of the previous conditions are True (1)
    # In this case, we would reach here only if the user does not eat pizza and does not exercise
    print("Unfit - No pizza but no exercise too!")