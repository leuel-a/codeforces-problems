from typing import List
from collections import defaultdict


def solve():
    w, h, n = map(int, input().split())

    # Now let us create a function that will tell us if
    # a given rectangle can be packed in a given area
    def good_square(size: int, w: int, h: int, n: int) -> bool:
        """Returns True if a square of size `size` can pack `n` rectangles of width `w` and height `h`"""
        return (size // w) * (size // h) >= n
    
    l = 1
    r = max(w, h) * n

    while r > l + 1:
        mid = l + (r - l) // 2

        if good_square(mid, w, h, n):
            r = mid
        else:
            l = mid

    print(r)

solve()