file_path = '071_080/file_test.txt'

try:
    with open(file_path, 'r') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += len(words)
        print(f"Số lượng từ trong file: {word_count}")
except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")