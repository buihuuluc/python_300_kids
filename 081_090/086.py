class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi

    def show_info(self):
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điêm tb: {self.diem_tb}")
        print(f"Địa chỉ: {self.dia_chi}")
        self._xep_loai()

    def xep_loai(self):
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung Bình"
        else:
            return "Yếu"

    def _xep_loai(self):
        loai = self.xep_loai()
        print(f"Xếp loại: {loai}")

hs = HocSinh("Bùi Hữu Lực", 18, 9.0, "17B Nguyễn Ngọc Sanh")
hs.show_info()