def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1/ exponent
    return result

try:
    base = float(input("Nhap co so: "))
    exponent = int(input("Nhap so mu: "))
    print(f"{base}^{exponent} = {power(base, exponent)}")
except ValueError:
    print("Vui long nhap so nguyen hop le.")