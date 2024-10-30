def songuyento(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6 
    return True

try:
    number = int(input("Nhập 1 số nguyên: "))
    if songuyento(number):
        print(f"Số {number} là số nguyên tố.")
    else:
        print(f"Số {number} không là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập đúng số nguyên.")
        