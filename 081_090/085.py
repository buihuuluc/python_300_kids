class HocSinh:
    def __init__(self, ten, tuoi, diemtb, diachi):
        self.ten = ten
        self._tuoi = tuoi
        self.diemtb = diemtb
        self._diachi = diachi

    def show_info(self):
        print(f"Hoc sinh: {self.ten}")
        print(f"Tuoi: {self._tuoi}")
        print(f"Diem trung binh: {self.diemtb}")
        print(f"Dia chi: {self._diachi}")

    def xeploai(self):
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
    
    # Getter cho thuộc tính private _tuoi
    @property
    def tuoi(self):
        return self._tuoi
    
    # Setter cho thuộc tính private _tuoi
    @tuoi.setter
    def tuoi(self, tuoi_moi):
        if tuoi_moi > 0:
            self._tuoi = tuoi_moi

    # Getter cho thuộc tính private _diachi
    def get_dia_chi(self):
        return self._diachi
    
    # Setter cho thuộc tính private _diachi
    def set_dia_chi(self, dia_chi_moi):
        self._diachi = dia_chi_moi

hs = HocSinh("Bùi Hữu Lực", 18, 8.2, "17B Nguyễn Ngọc Sanh")
#  Truy cập & thay đổi các giá trị thuộc tính public
print(f"Trước khi thay đổi:\n Tên: {hs.ten}, Điểm: {hs.diemtb}")
hs.ten = "Nguyễn Kim Tuyền"
hs.diemtb = 9.0
print(f"Sau khi thay đổi:\n Tên: {hs.ten}, Điểm trung bình: {hs.diemtb}")


# Truy cập & thay đổi các giá trị thuộc tính private qua getter và setter
print(f"Trước khi thay đổi:\n Tuổi: {hs.tuoi}, Địa chỉ: {hs.get_dia_chi()}")
hs.tuoi = 17
hs.set_dia_chi("233 Lê Lợi")
print(f"Sau khi thay đổi:\n Tuổi: {hs.tuoi}, Địa chỉ: {hs.get_dia_chi()}")