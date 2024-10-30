def calculate_fee(km):
    if km <= 1:
        fee = 10000
    elif km <= 10:
        fee = 10000 + (km-1)*8500
    else:
        fee = 10000 + 9 * 8500 + (km-10) * 7500

    return fee

try:
    km = float(input("Nhập số km đã đi: "))
    if km < 0:
        print("Nhập sai.")
    else:
        ketqua = calculate_fee(km)
        print(f"Số km đã đi: {km}, Số tiền là: {ketqua}")

except ValueError:
    print("Vui lòng nhập số đúng.")