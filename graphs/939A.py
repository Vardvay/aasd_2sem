n = int(input())
f = [0] * (n + 1)
values = list(map(int, input().split()))
for i in range(1, n + 1):
    f[i] = values[i - 1]

for i in range(1, n + 1):
    a = f[i]
    b = f[a]
    c = f[b]
    if c == i:
        print("YES")
        break
else:
    print("NO")