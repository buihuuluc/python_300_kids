def tinhgiaithua(n):
    if n < 0:
        return "Giai thừa không xác định cho số âm."
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

try:
    number = int(input("Nhập một số nguyên dương: "))
    if number < 0:
        print("Giai thừa không xác định cho số âm.")
    else:
        print(f"Giai thừa của {number} là: {tinhgiaithua(number)}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")