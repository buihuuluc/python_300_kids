file_path = '071_080/file_test.txt'

content_to_add = "\nTo day is the beautiful day."

try:
    with open(file_path, 'a') as file:
        file.write(content_to_add)
    print(f"Noi dung da duoc them vao file: {file_path}.")
    print(file_path.read())
except FileNotFoundError:
    print(f"Khong tim thay file: {file_path}")
except Exception as e:
    print(f"Da xay ra loi: {e}")