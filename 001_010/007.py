def tinhnamnhuan(nam):
    if (nam % 4 == 0 and nam % 100 !=0) or (nam % 400 == 0):
        return True
    else:
        return False
    
try:
    nam = int(input("Nhập năm: "))
    if nam <= 0 :
        print("Nhập năm sai, năm không thể nhỏ hơn 0.")
    else:
        if tinhnamnhuan(nam):
            print(f"Năm {nam} là năm Nhuận")
        else:
            print(f"Năm {nam} không là năm Nhuận.")
except ValueError:
    print("Nhập sai, vui lòng nhập lại.")