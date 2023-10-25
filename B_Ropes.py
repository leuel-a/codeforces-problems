from typing import List, Optional, Tuple, Dict
from collections import defaultdict, deque, Counter

"""This is a Binary Search Made For Real Numbers instead of integers
This is import to learn because you need to learn this for competitive programming
"""

def solve():
    n, k = map(int, input().split())
    ropes = []

    for _ in range(n):
        ropes.append(int(input()))

    def good_length(length: int, ropes: List[int], n: int, k: int) -> bool:
        return sum([rope // length for rope in ropes]) >= k
    
    l = 0
    r = 10e8

    for _ in range(100):
        mid = (l + r) / 2

        if good_length(mid, ropes, n, k):
            l = mid
        else:
            r = mid
    print(l)

solve()
