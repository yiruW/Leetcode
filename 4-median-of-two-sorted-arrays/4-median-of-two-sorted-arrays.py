class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return (nums[len(nums)>>1] + nums[(len(nums)-1)>>1])/2.0