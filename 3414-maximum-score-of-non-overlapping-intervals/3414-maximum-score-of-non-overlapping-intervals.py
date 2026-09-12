from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]

        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            """
            Return better result between:
            a = (score, indices)
            b = (score, indices)

            Higher score wins.
            If scores tie, lexicographically smaller indices wins.
            """
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            l, r, w, original_idx = arr[i - 1]

            j = bisect_right(ends, l - 1, 0, i - 1)

            for k in range(1, 5):

                not_take = dp[i - 1][k]

                prev_score, prev_indices = dp[j][k - 1]

                new_indices = sorted(prev_indices + [original_idx])

                take = (
                    prev_score + w,
                    new_indices
                )

                dp[i][k] = better(not_take, take)

        return dp[n][4][1]
        