import random

mylist = [random.randint(1, 100) for i in range(15)]

print(mylist)

mylist.sort()

print("After sort: ", mylist)