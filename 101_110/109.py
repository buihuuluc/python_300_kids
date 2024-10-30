import re

def loaibokytudacbiet(chuoi):
    ketqua = re.sub(r'[^A-Za-z0-9]', '', chuoi)
    return ketqua

chuoibandau = "Hello, World! Đây là một chuỗi #123 với ký tự đặc biệt @2024."

chuoiketqua = loaibokytudacbiet(chuoibandau)
print(chuoiketqua)