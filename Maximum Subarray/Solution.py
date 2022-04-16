class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        beg = 0
        end = 0
        curr = 0
        curr_max = nums[0]

        for i in range(0, len(nums)):
            curr_sum += nums[i]
            if curr_sum > curr_max:
                curr_max = curr_sum
                beg = curr
                end = i

            if curr_sum < 0:
                curr_sum = 0
                curr = i + 1
        return curr_max
