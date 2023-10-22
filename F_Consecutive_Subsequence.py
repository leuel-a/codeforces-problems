def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [1 for _ in range(n)]
    result = [[i] for i in range(1, n + 1)]
    last_index = {}  # Store the last index of every number.

    for i in range(n):
        # Check if arr[i]-1 exists in the last_index.
        if arr[i] - 1 in last_index:
            j = last_index[arr[i] - 1]
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                result[i] = [*result[j]] + [i + 1]

        # Update the last index for the current number.
        last_index[arr[i]] = i

    idx, length = max(enumerate(dp), key=lambda x: x[1])  # Find the index with the maximum length.
    print(length)
    print(*result[idx])

solve()
