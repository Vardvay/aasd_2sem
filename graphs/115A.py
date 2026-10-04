n = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = int(input())

answer = 0
for i in range(1, n + 1):
    cur = i
    depth = 0
    while cur != -1:
        depth += 1
        cur = parent[cur]
    if depth > answer:
        answer = depth

print(answer)