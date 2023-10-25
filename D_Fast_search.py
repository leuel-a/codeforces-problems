from typing import List
from collections import defaultdict, deque, Counter


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    a.sort()

    queries = []
    for _ in range(k):
        x, y = map(int, input().split())
        queries.append([x, y])

    result = []
    
    for x, y in queries:
        l = -1
        r = n

        # First search the left bound
        while r > l + 1:
            mid = (l + r) // 2

            # Invariants --> a[l] < target and a[r] >= target
            if a[mid] >= x:
                r = mid
            else:
                l = mid
        left_bound = r

        l = -1
        r = n
        
        # Search the right bound
        while r > l + 1:
            mid = (l + r) // 2

            # Invariants --> a[l] <= target and a[r] > target
            if a[mid] <= y:
                l = mid
            else:
                r = mid
        right_bound = l

        result.append(right_bound - left_bound + 1)

    print(*result)



solve()