
def check_num(n):
    if n > 0:
        return "Số nguyên dương."
    elif n < 0:
        return "Số nguyên âm."
    else:
        return "0 không là số dương, cũng không là số âm."
    
try:
    sonhap = int(input("Nhập một số nguyên bất kỳ: "))
    ketqua  = check_num(sonhap)
    print(ketqua)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")
