file_path = '071_080/file_test.txt'

try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print(f"File {file_path} khong ton tai.")
except Exception as e:
    print(f"Da xay ra loi {e}")