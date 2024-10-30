import re

# # Cach 1
def thaythetu(chuoi, tucu, tumoi):
    chuoimoi = chuoi.replace(tucu, tumoi)
    return chuoimoi

# Cach 2, 
# def thay_the_tu(chuoi, tu_cu, tu_moi):
#     """
#     Hàm để thay thế một từ trong chuỗi bằng từ khác sử dụng biểu thức chính quy.
#     """
#     chuoi_ket_qua = re.sub(r'\b{}\b'.format(re.escape(tu_cu)), tu_moi, chuoi)
#     return chuoi_ket_qua

chuoibandau = "Hello, I'm Luke"
old_tu = "Hello"
new_tu = "Hi"

# chuoiketqua1 = thaythetu(chuoibandau1, tu_cu, tu_moi)
# print(chuoiketqua1)

chuoiketqua = thaythetu(chuoibandau, old_tu, new_tu)
print(chuoiketqua)




