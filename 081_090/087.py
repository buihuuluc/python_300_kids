class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def show_info(self):
        print(f"Tên: {self.ten}")
        print(f"Tuổi: {self.tuoi}")

class HocSinh(Nguoi):
    def __init__(self, ten, tuoi, lop, diemtb):
        super().__init__(ten, tuoi)
        self.lop = lop
        self.diemtb = diemtb
    
    def show_info(self):
        super().show_info()
        print(f"Lớp: {self.lop}")
        print(f"Diểm trung bình: {self.diemtb}")

    def xep_loai(self):
        if self.diemtb >= 8.5:
            return "Giỏi"
        elif self.diemtb >= 6.5:
            return "Khá"
        elif self.diemtb >= 5:
            return "Trung Bình"
        else:
            return "Yếu"

hs = HocSinh("Bùi Hữu Lực", 16, "12B", 8.2)

hs.show_info()
print(f"Xếp loại: {hs.xep_loai()}")