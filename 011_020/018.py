def c_to_f(doc):
    return doc * 9 / 5 + 32

try:
    celcius = float(input("Nhap nhiet do C: "))
    dof = c_to_f(celcius)
    print(f"Do F la: {dof}")
except ValueError:
    print("Vui long nhap gia tri hop le.")