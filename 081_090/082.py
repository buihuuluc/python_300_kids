class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, diachi):
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.diachi = diachi

    def hien_thi_info(self):
        print(f"Hoc sinh: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Diem trung binh: {self.diem_tb}")
        print(f"Dia chi: {self.diachi}")

    def xeploai(self):
        if self.diem_tb >= 8.5:
            return "Gioi"
        elif self.diem_tb >= 6.5:
            return "Kha"
        elif self.diem_tb >= 5:
            return "Trung Binh"
        else:
            return "Yeu"
        
hs = HocSinh("Bui Huu Luc", 18, 7.6, "17B Nguyen Ngoc Sanh")
hs.hien_thi_info()
print(f"Xep loai: {hs.xeploai()}")