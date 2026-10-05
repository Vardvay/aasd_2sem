n = int(input())
db = {}

for _ in range(n):
    name = input().strip()
    if name in db:
        count = db[name]
        print(f"{name}{count}")
        db[name] += 1
    else:
        print("OK")
        db[name] = 1