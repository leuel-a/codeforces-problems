from typing import List
from collections import defaultdict


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    def closest_right(nums: List[int], target: int) -> int:
        l, r = -1, len(nums)

        # invariants: nums[l] <= target, nums[r] > target
        while r > l + 1:
            mid = (l + r) // 2

            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        return r

    for target in queries:
        result = closest_right(arr, target)
        print(result + 1)


solve()