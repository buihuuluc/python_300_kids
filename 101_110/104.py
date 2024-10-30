def doc_file1(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        noidung = file.read()
    return noidung

def timtudainhat(file_name):
    noidung = doc_file1(file_name)

    danh_sach_tu = noidung.split()

    do_dai_max = 0
    for tu in danh_sach_tu:
        if len(tu) > do_dai_max:
            do_dai_max = len(tu)

    tu_dai_nhat = [tu for tu in danh_sach_tu if len(tu) == do_dai_max]
    return tu_dai_nhat



# Cach 2

def doc_file2(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        noidung = file.read()
    return noidung

def tim_tu_dai_nhat(file_name):
    noidung = doc_file2(file_name)
    list_tu = noidung.split()
    do_dai_max = len(max(list_tu, key=len))
    tu_dai_nhat = [tu for tu in list_tu if len(tu) == do_dai_max]

    return tu_dai_nhat

file_name = "121_130/example.txt"
tudainhat = tim_tu_dai_nhat(file_name=file_name)
print(f"Tu dai nhat la: {tudainhat}")