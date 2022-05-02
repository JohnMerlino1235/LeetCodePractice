class Solution:
    def rob(self, nums: List[int]) -> int:
        # All houses arranged in a circle
        # If two adjacent houses are broken into the same night -> police get contacted
        # Return max amount of money you can rob without alerting the police
        # First index and last index are adjacent

        # EX: 2 -> 3 -> 2 -> 2

        def rob_helper(nums):
            last_house = 0
            two_houses_down = 0

            for n in nums:
                robbed = max(n + two_houses_down, last_house)
                two_houses_down = last_house
                last_house = robbed

            return last_house

        # 3 edge cases:
        # 1 -> Nums is 1 element
        # 2 -> Cannot contain the first index
        # 3 -> Cannot contain the last index

        return max(nums[0], rob_helper(nums[1:]), rob_helper(nums[:-1]))