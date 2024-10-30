my_dict = {
    'name': 'Luke',
    'age': 32,
    'city': 'Ca Mau'
}

print("Dict: ",my_dict)

key = input("Nhap key can kiem tra: ")

if key in my_dict:
    value = my_dict[key]
    print(f"Gia tri cua khoa '{key}' la: {value}")
else:
    print(f"Khoa {key} not in Dictionary.")