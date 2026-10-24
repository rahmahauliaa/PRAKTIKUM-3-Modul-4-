n = int(input())

for i in range(1, n + 1, 2):
    print(i, end=" ")
print()

start_genap = n if n % 2 == 0 else n - 1
for i in range(start_genap, 1, -2):
    print(i, end=" ")
print()