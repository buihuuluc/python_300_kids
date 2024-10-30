import os

file_path = '071_080/file_test.txt'

if os.path.isfile(file_path):
    print("File ton tai.")
else:
    print("File khong ton tai.")