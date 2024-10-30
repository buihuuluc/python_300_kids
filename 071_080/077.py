import os

file_path = '071_080/file_test.txt'

try:
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File: {file_path} da duoc xoa")
    else:
        print(f'File {file_path} khong ton tai.')
except Exception as e:
    print(f'Da xay ra loi: {e}')