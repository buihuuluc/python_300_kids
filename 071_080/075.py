file_path = '071_080/file_test.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        filttered =  ''.join(i for i in content if i not in (' ', '\n', '\t'))
        c_count = len(filttered)
        print(f"So ky tu la: {c_count}")
except FileNotFoundError:
    print("Can not find ",file_path)
except Exception as e:
    print("Error: ",e)