class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in dic:
                return [index, dic[complement]]
            dic[nums[index]] = index