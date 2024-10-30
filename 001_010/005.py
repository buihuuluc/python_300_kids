def tinh_diemtrungbinh(diems):
    return sum(diems)/ len(diems)

def tinh_phanloai(dtb):
    if dtb == 10: return "Xuat Sac"
    elif dtb >= 8.5: return "Gioi"
    elif dtb >= 6.5: return "Kha"
    elif dtb >= 5.0: return "Trung Binh" 
    else: return "Yeu"

try:
    scores = []
    somonhoc = int(input("So luong mon hoc: "))
    if somonhoc <=0 :
        print("So mon hoc phai lon hon 0")
    else:
        for i in range(somonhoc):
            diem = float(input(f"Nhap diem mon thu {i+1}: "))
            if diem < 0 :
                print("Nhap sai")
                break
            else:
                scores.append(diem)
        if len(scores) == somonhoc:
            diemtrungbinh = tinh_diemtrungbinh(scores)
            phanloai = tinh_phanloai(diemtrungbinh)
            print(f"Diem trung binh: {diemtrungbinh}")
            print(f"Phan loai: {phanloai}")

except ValueError:
    print("Nhap Sai, vui long nhap lai")
