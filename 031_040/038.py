my_tuple = (10, 20, 30, 20, 50, 60, 70, 80, 20, 40)

print("Tuple: ", my_tuple)
element = input("Nhap phan tu can dem so lan xuat hien: ")

try:
    element = int(element)
except ValueError:
    try:
        element = float(element)
    except ValueError:
        pass

count = my_tuple.count(element)

print(f"Phan tu: {element} xuat hien {count} lan trong tuple.")