class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result ={}
        for ind,ele in enumerate(nums):
            if target - ele in result:
                return [result[target-ele],ind]
            result[ele]=ind
