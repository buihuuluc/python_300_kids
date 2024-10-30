import re
def dem_so_cau(doan_van):
    # Sử dụng regex để tách đoạn văn thành các câu
    cau = re.split(r'[.?!]', doan_van)
    cau = [c for c in cau if c.strip()]
    return len(cau)


# Cach 2

def dem_so_cau_2(doan_van):
    so_cau = 0
    dau_cau = {'.','?','!'}

    for kytu in doan_van:
        if kytu in dau_cau:
            so_cau += 1

    return so_cau

doan_van = input("Nhap mot doan van: ")
so_cau = dem_so_cau_2(doan_van)
print(f"So cau la: {so_cau}")