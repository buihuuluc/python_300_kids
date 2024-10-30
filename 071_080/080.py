source_file = '071_080/file_test.txt'
destination_file = '071_080/example.txt'

try:
    with open(source_file, 'r') as sou_f:
        content = sou_f.read()

    with open(destination_file, 'a') as des_f:
        des_f.write(content)

    print(f"Noi dung tu file: {source_file} da sao chep thanh cong vao file: {destination_file}.")
except FileNotFoundError:
    print(f"Khong tim thay file: {source_file} or {destination_file}")
except Exception as e:
    print(f"Da xay ra loi {e}")
