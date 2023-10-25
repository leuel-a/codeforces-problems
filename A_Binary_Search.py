from typing import List
from collections import defaultdict


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    def binary_search(nums: List[int], target: int) -> int:
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    for target in queries:
        result = binary_search(arr, target)
        print('YES' if result != -1 else 'NO')    

solve()