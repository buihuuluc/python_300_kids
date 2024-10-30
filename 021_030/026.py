import random

my_list = [random.randint(1, 100) for i in range(20)]

print(my_list)
my_list.sort(reverse=True)
print("Reversed: ", my_list)