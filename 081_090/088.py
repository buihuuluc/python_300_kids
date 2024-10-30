class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    
    def show_info(self):
        print(f"Ten: {self.ten}")
        print(f"Tuoi: {self.tuoi}")

class HocSinh(Nguoi):
    def __init__(self, ten, tuoi, lop, diemtb):
        super().__init__(ten, tuoi)
        self.lop = lop
        self.diemtb = diemtb

    def show_info(self):
        super().show_info()
        print(f"Lop: {self.lop}")
        print(f"Diem trung binh: {self.diemtb}")

hs = HocSinh("Bui Huu Luc", 16, "10A1", 8.2)

hs.show_info()