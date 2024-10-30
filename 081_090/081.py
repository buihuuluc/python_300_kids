class HocSinh:
    def __init__(self, ten, tuoi, diem_tb):
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb

    def hienthithongtin(self):
        print(f"Hoc sinh: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Diem trung binh: {self.diem_tb}")

    def xeploai(self):
        if self.diem_tb >= 8.5:
            return "Gioi"
        elif self.diem_tb >= 6.5:
            return "Kha"
        elif self.diem_tb >= 5:
            return "Trung Binh"
        else:
            return "Yeu"
        
hs = HocSinh("Bui Huu Luc", 32, 7)
hs.hienthithongtin()
print(f"Xep loai: {hs.xeploai()}")