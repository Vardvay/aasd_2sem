def main():
    t = int(input())
    out = []

    for _ in range(t):
        n, m = map(int, input().split())

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        depth = [-1] * (n + 1)
        depth[1] = 0
        q = [1]
        head = 0
        even = []
        odd = []

        while head < len(q):
            u = q[head]
            head += 1
            if depth[u] % 2 == 0:
                even.append(u)
            else:
                odd.append(u)
            for v in adj[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    q.append(v)

        chosen = even if len(even) <= len(odd) else odd
        out.append(str(len(chosen)))
        out.append(" ".join(map(str, chosen)))

    print("\n".join(out))

main()