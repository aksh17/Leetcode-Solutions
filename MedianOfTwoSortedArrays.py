class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = nums1+nums2
        nums1.sort()
        if len(nums1)%2 == 0:
            ind = ((nums1[len(nums1)/2] + nums1[(len(nums1)/2)-1])/float(2))
            return ind
        else:
            ind = float(nums1[(len(nums1)-1)/2])
            return ind