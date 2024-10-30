def dem_so_tu(chuoi):

    danhsach_tu = chuoi.split()
    so_tu = len(danhsach_tu)

    return so_tu

chuoi = input("Nhap 1 chuoi: ")

sotu = dem_so_tu(chuoi)

print("So tu trong chuoi la: ", sotu)