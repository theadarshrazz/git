n = int(input("Enter The Number :- "))

bus = list(map(int, input().split()))

bus.sort()

result = []
i = 0

while i < n:
    start = i

    while i + 1 < n and bus[i + 1] == bus[i] + 1:
        i += 1

    end = i

    if end - start >= 2:
        result.append(f"{bus[start]}-{bus[end]}")
    else:
        for j in range(start, end + 1):
            result.append(str(bus[j]))

    i += 1

print(" ".join(result))
