class HocSinh:
    def __init__(self, ten, tuoi, diemtb, diachi):
        self.ten = ten
        self.tuoi = tuoi
        self.diemtb = diemtb
        self.diachi = diachi

    def show_info(self):
        print(f"Hoc sinh: {self.ten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Diem TB: {self.diemtb}")
        print(f"Dia chi: {self.diachi}")

    def xeploai(self):
        if self.diemtb >= 8.5:
            return "Gioi"
        elif self.diemtb >= 6.5:
            return "Kha"
        elif self.diemtb >= 5.0:
            return "Trung Binh"
        else:
            return "Yeu"
        
    def update_diemtb(self, diemmoi):
        self.diemtb = diemmoi
        print(f"Diem trung binh moi cua hoc sinh {self.ten} la {self.diemtb}")
    
    def loi_chao(self):
        print(f"Xin chao! toi la {self.ten} va toi hoc lop 12. Rat vui duoc gap cac ban.")


hs = HocSinh("Bui Huu Luc", 18, 8.0, "17B Nguyen Ngoc Sanh")

hs.loi_chao()
hs.show_info()
print(f"Xep loai: {hs.xeploai()}")
hs.update_diemtb(9.0)
hs.show_info()
print(f"Xep loai: {hs.xeploai()}")