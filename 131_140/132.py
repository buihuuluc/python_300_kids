def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(char) ** 2 for char in str(n))
    return n == 1

def first_happy_number(n):
    happy_numbers = []
    num = 1
    while (len(happy_numbers) < n):
        if is_happy_number(num):
            happy_numbers.append(num)
        num += 1
    return happy_numbers

n = 20

happy_numbers  = first_happy_number(n)
print(f"10 so hanh phuc dau tien: {happy_numbers}")