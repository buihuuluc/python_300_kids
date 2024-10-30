import math
def lcm(a, b):
    return abs(a * b) //math.gcd(a, b)

a = 10
b  = 20

bscnn = lcm(a, b)
print(f"Bội số chung nhỏ nhất của {a} và {b} là: {bscnn}")