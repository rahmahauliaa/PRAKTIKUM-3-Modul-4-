n, k = map(int, input().split())

total_semua = 0

for i in range(1, n + 1):
    jumlah = 0
    deret = []
    for j in range(i, 0, -1):
        deret.append(f"({j} * {k})")
        jumlah += j * k
    
    print(" + ".join(deret) + f" = {jumlah}")
    total_semua += jumlah

print(total_semua)