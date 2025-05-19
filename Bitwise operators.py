a = 10  # Binary: 1010 
b = 4   # Binary: 0100

""" 
Bitwise AND:
  1010
& 0100
------
  0000 → 0
"""
print("a & b:", a & b)

""" 
Bitwise OR:
  1010
| 0100
------
  1110 → 14 "It will be changed to binary to deciamal"
"""
print("a | b:", a | b)

""" 
Bitwise XOR:
  1010
^ 0100
------
  1110 → 14
"""
print("a ^ b:", a ^ b)

""" 
Bitwise NOT:
~a → -(a + 1)
~10 → -(10 + 1) = -11
"""
print("~a:", ~a)

""" 
Left Shift:
1010 << 1 = 10100 → 20
"""
print("a << 1:", a << 1)

""" 
Right Shift:
1010 >> 1 = 0101 → 5
"""
print("a >> 1:", a >> 1)