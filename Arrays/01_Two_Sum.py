class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}

        for i, x in enumerate(nums):
            comp = target - x
            if comp in lookup:
                return(lookup[comp],i)
            lookup[x] = i