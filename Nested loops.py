# Nested loop example: Print a right-angled triangle pattern

rows = 4  # Number of rows

for i in range(1, rows + 1):  # Outer loop controls the number of rows
    for j in range(1, i + 1):  # Inner loop controls stars per row
        print("*", end=" ")   # Print star with space, stay on same line
    print()  # Move to the next line after each row
# Output:
# *
# * *
# * * *
# * * * *