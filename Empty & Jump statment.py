# Example of pass statement
print("Pass statement example:")
for i in range(3):
    if i == 1:
        pass  # 'pass' does nothing; it's just a placeholder
    print("i =", i)  # Still prints even if pass is used

# Example of continue statement
print("\nContinue statement example:")
for j in range(5):
    if j == 2:
        continue  # Skips the rest of the loop when j == 2
    print("j =", j)  # Will not print j = 2

# Example of break statement
print("\nBreak statement example:")
for k in range(5):
    if k == 3:
        break  # Exits the loop completely when k == 3
    print("k =", k)  # Will only print until k = 2
