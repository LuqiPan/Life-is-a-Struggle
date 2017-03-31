class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # [1,2]
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        result = []
        for num in nums:
            new_nums = list(nums)
            new_nums.remove(num)
            result += [[num] + perm for perm in self.permute(new_nums)]
        return result

s = Solution()
print s.permute([])
print s.permute([1])
print s.permute([1, 2])
