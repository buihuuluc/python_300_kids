def check_even_ood(n):
    if n % 2 == 0:
        return "Số chẵn."
    else: return "Số lẻ."

try: 
    sokiemtra = int(input("Nhập 1 số nguyên: "))
    ketqua = check_even_ood(sokiemtra)
    print(ketqua)
except ValueError:
    print("Nhập sai rồi ba.")
    