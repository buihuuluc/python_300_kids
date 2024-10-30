def ucln(a,b):
    while b != 0:
        a, b = b, a % b
    return a

try:
    a = int(input("Nhập số thứ 1: "))
    b = int(input("Nhập số thứ 2: "))
    uoclonnhat = ucln(a, b)
    print(f"Ước số chung lớn nhất của {a} và {b} là: {uoclonnhat}")
except ValueError:
    print("Nhập số nguyên.")