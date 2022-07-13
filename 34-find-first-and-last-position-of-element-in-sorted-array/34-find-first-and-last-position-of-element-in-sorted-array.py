class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findLeftBound(nums, target):
            left, right = 0, len(nums) - 1
            leftBound = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle - 1
                    leftBound = right
                else:
                    left = middle + 1
            print(leftBound)
            return leftBound
        
        def findRightBound(nums, target):
            left, right = 0, len(nums) - 1
            rightBound = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] <= target:
                    left = middle + 1
                    rightBound = left
                else:
                    right = middle -1
            print(rightBound)
            return rightBound
        
        left = findLeftBound(nums, target)
        right = findRightBound(nums, target)
        
        if left == -2 or right == -2:
            return [-1, -1]
        elif right - left > 1:
            return [left + 1, right - 1]
        else:
            return [-1, -1]
        