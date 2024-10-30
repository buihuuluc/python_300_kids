def dem_chan_le(numbers):
    sochan = 0
    sole = 0
    for num in numbers:
        if num % 2 == 0:
            sochan += 1
        else: sole += 1
    return sochan, sole

try:
    day = input("Nhập dãy số, cách biệt bằng dấu cách: ")
    dayso = [int(num) for num in day.split()]
    sochan, sole = dem_chan_le(dayso)
    print(f"Số chẵn là: {sochan}")
    print(f"Số lẻ: {sole}")
except ValueError:
    print("Nhập sai, vui lòng nhập lại.")
        