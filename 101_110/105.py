def doc_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        noi_dung = file.read()
    return noi_dung

def tim_tu_xuat_hien_nhieu_nhat(file_name):
    noidung = doc_file(file_name)

    list_tu = noidung.split()
    print(list_tu)
    tu_dem = {}
    for tu in list_tu:
        tu = tu.lower().strip('.,!?:;()[]')
        if tu in tu_dem:
            tu_dem[tu] += 1
        else:
            tu_dem[tu] = 1
    print(tu_dem)
    tu_nhieu_nhat = max(tu_dem, key=tu_dem.get)

    return tu_nhieu_nhat, tu_dem[tu_nhieu_nhat]

file_name = '121_130/example.txt'

tu_nhieu_nhat, so_lan_xuat_hien = tim_tu_xuat_hien_nhieu_nhat(file_name)

print(f"Tu xuat hien nhieu nhat la: '{tu_nhieu_nhat}', so lan xuat hien la: {so_lan_xuat_hien}")