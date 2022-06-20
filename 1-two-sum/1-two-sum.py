class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}
        
        for i in range(len(nums)):
            remaining = target - nums[i]
            
            if remaining in seen: 
                return [seen[remaining], i]
            else:
                seen[nums[i]] = i
    