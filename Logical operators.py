age = 20
has_ticket = True
is_drunk = False
is_vip = False

# Using `and`
if age >= 18 and has_ticket:
    print("You can enter ")

# Using `or`
if has_ticket or is_vip:
    print("You can enter ")

# Using `not`
if not is_drunk:
    print("You are not drunk, entry allowed ")

# Using all the logical operators 

age = 20
has_ticket = False
is_vip = True
is_drunk = False

# Using: and, or, not
if (age >= 18 and not is_drunk) and (has_ticket or is_vip):
    print("You can enter!")
else:
    print("Entry not allowed.")
