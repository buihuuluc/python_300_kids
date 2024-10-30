def find_max_of_three(a, b, c):
    if a>=b and a >=c:
        return a
    elif b>=a and b>=c:
        return b
    else: return c

try: 
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    ketqua = find_max_of_three(a, b, c)
    print(f"Số lớn nhất là: {ketqua}")
except ValueError:
    print("Nhập sai rồi ba.")