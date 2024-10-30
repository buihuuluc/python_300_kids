import random 

mylist = [random.randint(1, 100) for i in range(10)]

print(mylist)
rmove = input("Nhập phần tử muốn xóa: ")

try:
    rmove = int(rmove)
except ValueError:
    try: 
        rmove = float(rmove)
    except ValueError:
        pass

if rmove in mylist:
    mylist.remove(rmove)
    print("Danh sách sau khi xóa phần tử: ", mylist)
else:
    print("Phần tử không tồn tại trong danh sách.")