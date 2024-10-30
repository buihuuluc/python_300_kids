my_tuple = (10, 20, 30, 40, 50)

print("Tuple: ",my_tuple)

element = input("Nhap phan tu can kiem tra: ")

try:
    element = int(element)
except ValueError:
    try:
        element = float(element)
    except ValueError:
        pass

if element in my_tuple:
    print(f"Phan tu {element} co trong tuple.")
else:
    print(f"Phan tu {element} khong co trong tuple.")