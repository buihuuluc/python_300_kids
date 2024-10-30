import random

mylist = [random.randint(1, 100) for i in range(10)]
print(mylist)

chen = input("Nhập nhần tử muốn chèn vào danh sách: ")
chen = int(chen)
mylist.append(0,chen)
print("Danh sách sau khi chèn thêm phần tử: ", mylist)
