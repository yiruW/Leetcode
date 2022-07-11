class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # since the array is ordered and no deplicate
        # we could apply binary search
        left = 0
        right = len(nums)-1
        
        while (left <= right):
            middle = left + (right - left) // 2
            if (nums[middle] == target):
                return middle
            if (nums[middle] < target):
                left = middle + 1
            elif (nums[middle] > target):
                right = middle - 1
            
        return -1
            