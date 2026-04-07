import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x == rep_y:
        return

    parents[rep_y] = rep_x
    return


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    elif command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
