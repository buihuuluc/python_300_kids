import random
my_list = [random.randint(1,100) for i in range(10)]

print(my_list)

min_elements = min(my_list)
print("Min elements: ",min_elements)