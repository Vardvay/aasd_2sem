import sys
sys.setrecursionlimit(300000)

def main():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    answer = 0

    def dfs(u, parent, cats):
        nonlocal answer
        is_leaf = True
        for v in adj[u]:
            if v == parent:
                continue
            is_leaf = False
            new_cats = cats + 1 if a[v] == 1 else 0
            if new_cats <= m:
                dfs(v, u, new_cats)
        if is_leaf and cats <= m:
            answer += 1

    if a[1] <= m:
        dfs(1, 0, a[1])

    print(answer)

main()