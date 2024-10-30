file_path = "071_file.txt"

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("Noi dung cua file: ")
        print(content)
except FileNotFoundError:
    print("Khong tim thay file: ",file_path)
except Exception as e:
    print("Da xay ra loi: ", e)