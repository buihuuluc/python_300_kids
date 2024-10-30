def file_read(source_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def tach_tu(source_file):
    content = file_read(source_file)
    list_char = content.split()

    return list_char

source_file = '121_130/example.txt'
list_tu = tach_tu(source_file)

print("Danh sach tu: ", list_tu)