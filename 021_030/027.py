import random

my_list = [random.randint(1, 100) for i in range(20)]
print(my_list)
max_element = max(my_list)

print("Max element: ", max_element)