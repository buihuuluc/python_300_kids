class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        """Phương thức khởi tạo để thiết lập các thuộc tính của học sinh"""
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        """Phương thức để hiển thị thông tin của học sinh"""
        print(f"Học sinh: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm trung bình: {self.diem_tb}")
        print(f"Địa chỉ: {self.dia_chi}")

    def xep_loai(self):
        """Phương thức để xếp loại học sinh dựa trên điểm trung bình"""
        if self.diem_tb >= 8.5:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

danh_sach_hoc_sinh = []
num_hs = int(input("So luong hoc sinh muon nhap: "))
for hocsinh in range(num_hs):
    print(f"Nhap thong tin hoc sinh thu {hocsinh + 1}: \n")
    ten = input("Nhap ten: ")
    tuoi = int(input("Tuoi: "))
    diemtb = float(input("Diem trung binh: "))
    diachi = input("Dia chi: ")
    hocsinh = HocSinh(ten, tuoi, diemtb, diachi)
    danh_sach_hoc_sinh.append(hocsinh)

for hoc_sinh in danh_sach_hoc_sinh:
    print("-----")
    hoc_sinh.hien_thi_thong_tin()
    print(f"Xếp loại: {hoc_sinh.xep_loai()}")
    print("-----")