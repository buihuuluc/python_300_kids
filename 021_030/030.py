list = input("Nhập chuỗi muốn kiểm tra (cách biệt bằng dấu cách): ")
try:
    list = int(list)
except ValueError:
    try:
        list = float(list)
    except ValueError:
        pass

print("Danh sách đã nhập: ", list)
phan_tu = input("Nhập phần tử muốn kiểm tra: ")
dem = list.count(phan_tu)

print(f'Phần tử "{phan_tu}" xuất hiện {dem} lần trong danh sách.')