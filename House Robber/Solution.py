class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Decision tree Rob House1 -> can either Rob House3/House4
        Two variables: Rob1 Rob2
        """
        rob1 = 0  # House before that
        rob2 = 0  # Last house we robbed

        for num in nums:
            current = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = current

        return rob2