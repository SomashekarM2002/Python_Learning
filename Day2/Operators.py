x = 5
x +=3
x-=2
x*=4
x/=6
# x%=5
print(x)

# Logical Operators Example

a = 10
b = 5

# AND Operator
print("AND Operator:", a > 5 and b > 2)

# OR Operator
print("OR Operator:", a > 5 or b < 2)

# NOT Operator
print("NOT Operator:", not(a > b))

# Bitwise Operators Example

a = 5   # 0101
b = 3   # 0011

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)