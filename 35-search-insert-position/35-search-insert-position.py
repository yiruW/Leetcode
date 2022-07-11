class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while (left <= right):
            middle = left + (right - left) // 2
            if (nums[middle] == target):
                return middle
            elif (nums[middle] > target):
                right = middle -1
            elif (nums[middle] < target):
                left = middle + 1
           
            
        return right + 1