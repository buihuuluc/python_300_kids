file_path = '071_080/file_test.txt'

try:
    # Mở file văn bản với chế độ đọc
    with open(file_path, 'r') as file:

        # Cách 1: Đếm số lượng dòng trong file
        line_count = sum(1 for line in file)

        # Cách 2: 
        # line_count = 0
        # for _ in file:
        #     line_count += 1

        # Cách 3:
        # lines = file.readlines()
        # line_count = len(lines)


        # In số lượng dòng
        print(f"Số lượng dòng trong file: {line_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")