def tinhtongchuso(n):
    total = 0
    n= abs(n)
    while n > 0:
        total += n %10
        n //= 10
    return total

try:
    number = int(input("Nhap so can tinh tong: "))
    print(f"Tong cac chu so cua {number} la: {tinhtongchuso(number)}")
except ValueError:
    print("Vui long nhap so nguyen hop le.")