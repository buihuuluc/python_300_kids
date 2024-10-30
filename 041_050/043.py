my_dict = {
    'name': 'Luke',
    'age': 32,
    'city': 'Ca Mau'
}

print(f"Dictionary ban dau: {my_dict}")

new_key = input("Nhap key: ")
new_value = input("Nhap gia tri: ")

my_dict[new_key] = new_value

print(f"Dictionary sau khi da them: {my_dict}")

