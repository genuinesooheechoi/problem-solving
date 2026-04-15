import sys
input = sys.stdin.readline

from heapq import heappush, heappop
max_heap = []

N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if max_heap:
            result = -heappop(max_heap)
            print(result)

        else:
            print(0)

    else:
        heappush(max_heap, -x)