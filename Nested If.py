# Nested If Example: Check if a student has passed a course based on marks and attendance
# Input marks and attendance percentage
marks = int(input("Enter your marks (0-100): "))
attendance = int(input("Enter your attendance percentage (0-100): "))

# Outer if: Check if marks are passing
if marks >= 40:
    # Inner if: Check if attendance is sufficient
    if attendance >= 75:
        print("You passed the course!")
    else:
        print("You failed due to low attendance.")
else:
    # Outer else: Marks are not passing
    print("You failed due to low marks.")
