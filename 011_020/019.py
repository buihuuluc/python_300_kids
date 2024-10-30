import math

def chuvi(bankinh):
    return 2 * math.pi * bankinh

def dientich(bankinh):
    return bankinh * bankinh * math.pi

try:
    bankinh = float(input("Nhap ban kinh: "))
    if bankinh < 0:
        print("Ban kinh khong the la so am.")
    else:
        cv = chuvi(bankinh)
        dt = dientich(bankinh)
        print("Chu vi la: ",cv)
        print("Dien tich la: ",dt)
except ValueError:
    print("Vui long nhap mot gia tri hop le cho ban kinh.")