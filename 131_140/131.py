# def fibonacci_for(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
    
#     fibo_seq = [0, 1]
#     for i in range(2, n):
#         next_fib = fibo_seq[-1] + fibo_seq[-2]
#         fibo_seq.append(next_fib)

#     return fibo_seq

# n = 100
# pFibo = fibonacci_for(n)
# print("Day fibo la: ",pFibo)

def laisuatkep(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1000]
    elif n == 2:
        return [1000,2000]
    laisuat_list = [1000, 2000]
    for i in range(2,n):
        next_i = laisuat_list[-1] * 2
        laisuat_list.append(next_i)
    return laisuat_list

n = 5
total = sum(laisuatkep(n))
print(f"So tien moi ngay: {laisuatkep(n)}")
print(f"Sau {n} ngay, so tien co duoc la: {total}")