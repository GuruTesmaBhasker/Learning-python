# Creating a set
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

a = {1, 2, 3}
b = {3, 4, 5}

# Adding an element
a.add(6)  # a becomes {1, 2, 3, 6}

# Removing an element
a.remove(2)  # a becomes {1, 3, 6}

#clearing a set
a.clear()  # a becomes set()

# Union
print(a | b)  # Output: {1, 3, 4, 5, 6}
print(a.union(b))  # Output: {1, 3, 4, 5, 6}

# Intersection
print(a & b)  # Output: {3}
print(a.intersection(b))  # Output: {3}

# Difference
print(a - b)  # Output: {1, 6}
print(a.difference(b))  # Output: {1, 6}

# Checking membership
print(3 in a)  # Output: True

