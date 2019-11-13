class Solution(object):
    def rotate(self, nums, k):
        i=0
        while i<k:
            p=nums[len(nums)-1]
            nums.pop(len(nums)-1)
            nums.insert(0,p)
            i+=1