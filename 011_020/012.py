def tong(n):
    if n < 1:
        print("Nhập số dương.")
    else:
        return n * (n +1) // 2
    
try:
    number = int(input("Nhập số n muốn tính tổng: "))
    if number < 1:
        print("Nhập số dương.")
    else:
        print(f"Tổng các số từ 1 đến {number} là: {tong(number)}")
except ValueError:
    print("Vui lòng nhập số nguyên.")