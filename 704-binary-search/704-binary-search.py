class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # since the array is ordered and no deplicate
        # we could apply binary search
        left = 0
        right = len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
            
        return -1
            