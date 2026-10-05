t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    counts = {}
    ans = 0
    
    for i in range(n):
        val = a[i] - i
        if val in counts:
            ans += counts[val]
            counts[val] += 1
        else:
            counts[val] = 1
            
    print(ans)