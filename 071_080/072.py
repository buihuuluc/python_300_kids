file_path = '071_080/file_test.txt'

content_to_write = "Hello, world!\nWelcome to the world of Python programming."

try:
    # Mở file văn bản với chế độ ghi
    with open(file_path, 'w') as file:
        # Ghi nội dung vào file
        file.write(content_to_write)
        # In thông báo ghi thành công
        print(f"Nội dung đã được ghi vào file: {file_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")