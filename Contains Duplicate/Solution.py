class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        index = 0
        while index < len(nums):
            if nums[index] not in dic:
                if index == len(nums) - 1:
                    return False
                else:
                    dic[nums[index]] = 1

            else:
                return True

            index += 1

