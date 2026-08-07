class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = list(accumulate(nums, initial=0))
        min_length = n + 1

        for i in range(n + 1):
            left, right = i, n
            first_true_index = -1
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] >= prefix_sums[i] + target:
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if first_true_index != -1:
                min_length = min(min_length, first_true_index - i)

        return min_length if min_length <= n else 0