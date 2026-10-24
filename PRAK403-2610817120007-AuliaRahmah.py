a, b = map(int, input().split())

i, j = a, b

if a < b:
    while i <= b and j >= a:
        print(f"{i} {j}", end="")
        if i < b:
            print(" - ", end="")
        i += 1
        j -= 1
else:
    while i >= b and j <= a:
        print(f"{i} {j}", end="")
        if i > b:
            print(" - ", end="")
        i -= 1
        j += 1
print()