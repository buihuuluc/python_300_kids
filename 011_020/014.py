def find_max(numbers):
    if not numbers:
        return "Danh sách rỗng."
    max_num = numbers[0]
    for i in numbers:
        if i >= max_num:
            max_num = i
    return max_num

try:
    input_numbers = input("Nhập các số trong danh sách, cách nhau bởi dấu cách: ")
    numbers = [float(num) for num in input_numbers.split()]

    if not numbers:
        print("Danh sách rỗng!.")
    else:
        max_number = find_max(numbers)
        print(f"Số lớn nhất trong chuỗi là: {max_number}.")
except ValueError:
    print("Vui lòng nhập đúng kiểu số.")