
from typing import List

class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int],
        k1: int, k2: int
    ) -> int:

        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diffs)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        
        used = sum(max(0, d - threshold) for d in diffs)
        remaining = k - used

        answer = sum(min(d, threshold) ** 2 for d in diffs)

        
        if threshold > 0:
            answer -= remaining * (2 * threshold - 1)

        return answer
